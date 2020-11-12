from readDat     import *
from element3d   import *
from pointsGauss import *
from matrixTools import *
from elementsTools import *
from visuTools   import *
from petsc4py             import PETSc
import time
E         = 200000.
nu        = 0.3
print('....Lecture du maillage et des groupes')
nodes,els = readDat('datas/poutre.dat')

nodeEnc   = readDat('datas/poutreEncastre.dat')
encas=map(lambda x:x.id(),nodeEnc[0].values())
nodeFor   = readDat('datas/poutreForce.dat')
force=map(lambda x:x.id(),nodeFor[0].values())

nnodes     = len(nodes)
ndofs      = nnodes*3
nnz       = computeNonZeroByRows(els,ndofs)
encastre  = []
for n in encas:
    encastre.append(dofNumberGlobal(n,0))
    encastre.append(dofNumberGlobal(n,1))
    encastre.append(dofNumberGlobal(n,2))
ddlAct = listActiveDofs(ndofs,encastre)
efforts=[]
for i in force:
     efforts.append(dofNumberGlobal(i,1))
     
values = zeros((len(encastre),),'d')
Fglob = PETSc.Vec().createSeq(ndofs)
Kglob = PETSc.Mat().create(PETSc.COMM_SELF)
Kglob.setSizes([ndofs,ndofs])
Kglob.setType(PETSc.Mat.Type.SEQAIJ)
Kglob.setPreallocationNNZ(nnz)
Kglob.setUp()
valeff = ones((len(efforts),))*1000.
Fglob.setValues(efforts,valeff,PETSc.InsertMode.INSERT)
Kglob.zeroEntries()
print('....Debut d assemblage')
for el in els:
      el.setMaterialProperties(E,nu)
      el.setGaussPointsAndWeights(GP2,WP2)
      kel   = el.stiffness()
      ddls  = el.ddls()
      Kglob.setValues(ddls,ddls,kel,PETSc.InsertMode.ADD)
print('....Fin d assemblage')
Kglob.assemble()
Kglob.zeroRows(encastre,1.)

# create linear solver
ksp=PETSc.KSP()
ksp.create(PETSc.COMM_WORLD)
# use conjugate gradients
ksp.setType('cg')
# and incomplete 
ksp.getPC().setType('icc')
du=Fglob.duplicate()
du.set(0.)
# and next solve
ksp.setOperators(Kglob)
ksp.setFromOptions()
print('....Resolution:K.u=F')
ksp.solve(Fglob,du)
Du = zeros((nnodes,3),'d')
for i,ddl in enumerate(du[:ndofs]):
    node,comp = nodeDdlNumber(i)
    Du[node,comp]  = ddl
# # print Du
sigmas  = []
for el in els:
     ddls = el.ddls()
     sigmas.append(el.computeStressesInElement(du[ddls]))

print('....Ecriture des resultats')
resFile = resultsFile("test.vtu")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
resFile.addVectorToCell(sigmas,'SIGM_ELNO')
resFile.write()
