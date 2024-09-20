from readDat     import *
from element3d   import *
from pointsGauss import *
from matrixTools import *
from elementsTools import *
from visuTools   import *
from petsc4py             import PETSc
from slepc4py             import SLEPc
import time

E         = 200000.
nu        = 0.3
rho       = 7.8e-6
print('....Lecture du maillage et des groupes')
nodes,els = readDat('datas/poutre.dat')

nodeEnc   = readDat('datas/poutreEncastre.dat')
encas=[x.id() for x in nodeEnc[0].values()]
nodeFor   = readDat('datas/poutreForce.dat')
force=[x.id() for x in nodeFor[0].values()]

nnodes     = len(nodes)
#activeDofs = np.delete(arange(nnodes),array(encas))

ndofs      = nnodes*3
print('-'*30,' Nbre de ddls:',ndofs)
nnz       = computeNonZeroByRows(els,ndofs)
encastre  = []
for n in encas:
    encastre.append(dofNumberGlobal(n,0))
    encastre.append(dofNumberGlobal(n,1))
    encastre.append(dofNumberGlobal(n,2))

ddlAct = listActiveDofs(ndofs,encastre)
ndofs = len(ddlAct)
Kglob = PETSc.Mat().create(PETSc.COMM_SELF)
Mglob = PETSc.Mat().create(PETSc.COMM_SELF)
Kglob.setSizes([ndofs,ndofs])
Kglob.setType(PETSc.Mat.Type.SEQAIJ)
Kglob.setPreallocationNNZ(nnz)

Kglob.setUp()
Mglob.setSizes([ndofs,ndofs])
Mglob.setType(PETSc.Mat.Type.SEQAIJ)
Mglob.setPreallocationNNZ(nnz)
Mglob.setUp()
Kglob.zeroEntries()
Mglob.zeroEntries()
Kglob.setOption(19,0)
Mglob.setOption(19,0)
tdeb = time.time()
print('....Debut d assemblage')
for el in els:
      el.setMaterialProperties(E,nu,rho)
      el.setGaussPointsAndWeights(GP2,WP2)
      kel      = el.stiffness()
      massel   = el.mass()
      ddls     = el.ddls()
      ddlocact,lact = activeDofs(ddls,ddlAct)
      #print(ddls,lact,ddlocact)
      kslic    = sliceSquareMatrix(kel,ddls,lact)
      mslic    = sliceSquareMatrix(massel,ddls,lact)
      Kglob.setValues(ddlocact,ddlocact,kslic,PETSc.InsertMode.ADD)
      Mglob.setValues(ddlocact,ddlocact,mslic,PETSc.InsertMode.ADD)
print('....Fin d assemblage')
Kglob.assemble()
Mglob.assemble()
xr, xi = Kglob.createVecs()

pc = PETSc.PC().create()
# pc.setType(pc.Type.HYPRE)
pc.setType(pc.Type.BJACOBI)
    
ksp = PETSc.KSP().create()
ksp.setType(ksp.Type.PREONLY)
ksp.setPC( pc )
    
    
#F = SLEPc.ST().create()
# F.setType(F.Type.PRECOND)
# F.setKSP( ksp )
# F.setShift(0)

# Setup the eigensolver
E = SLEPc.EPS().create()
#E.setST(F)
E.setOperators(Kglob,Mglob)
E.setType(E.Type.LOBPCG)
E.setDimensions(30)
E.setWhichEigenpairs(E.Which.SMALLEST_REAL)
E.setProblemType(SLEPc.EPS.ProblemType.GHEP)
E.setFromOptions()
# WK = PETSc.Viewer().createASCII('Kglob.txt')
# Kglob.view(WK)
# WM = PETSc.Viewer().createASCII('Mglob.txt')
# Mglob.view(WM)
# Solve the eigensystem
E.solve()

print("")
its = E.getIterationNumber()
print("Number of iterations of the method: %i" % its)
sol_type = E.getType()
print("Solution method: %s" % sol_type)
nev, ncv, mpd = E.getDimensions()
print("Number of requested eigenvalues: %i" % nev)
tol, maxit = E.getTolerances()
print("Stopping condition: tol=%.4g, maxit=%d" % (tol, maxit))
nconv = E.getConverged()
print("Number of converged eigenpairs: %d" % nconv)
omegas=[]
amps  = []
if nconv > 0:
    print("")
    print("        k          ||Ax-kx||/||kx|| ")
    print("----------------- ------------------")
    for i in range(nconv):
        k = E.getEigenpair(i, xr, xi)
        omegas.append(k.real)
        amps.append(xr.max()[1])
        error = E.computeError(i)
        if k.imag != 0.0:
          print(" %9f%+9f j  %12g" % (k.real, k.imag, error))
        else:
          print(" %12f       %12g" % (k.real, error))
print("")


print('-----Resolution en :',time.time()-tdeb,' s')

#for i,ddl in enumerate(du[:ndofs]):
#     node,comp      = nodeDdlNumber(i)
#     Du[node,comp]  = ddl
print('....Ecriture des resultats')
resFile = resultsFile("testpetsc.vtu")
resFile.defineMesh(nodes,els)
for im in range(nconv):
    E.getEigenpair(im,xr,xi)
    Du = zeros((nnodes,3),'d')
    for ii,i in enumerate(ddlAct):
        node,dd=nodeDdlNumber(i)
        Du[node,dd] = xr.getValue(ii)
    resFile.addVectorToNode(Du,'Mode '+str(im))

resFile.write()
sauv=zeros((len(omegas),2),'d')
print(omegas,amps)
sauv[:,0] = omegas
sauv[:,1] = amps

plot(omegas,amps)
show()
savetxt('om_amp.txt',sauv)
