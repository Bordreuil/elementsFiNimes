from readDat     import *
from element3d   import *
from pointsGauss import *
from matrixTools import *
from elementsTools import *
from visuTools   import *
import time
E         = 200000.
nu        = 0.3
print('....Lecture du maillage et des groupes')
nodes,els = readDat('datas/poutre.dat')

nodeEnc   = readDat('datas/poutreEncastre.dat')
encas=map(lambda x:x.id(),nodeEnc[0].values())
nodeFor   = readDat('datas/poutreForce.dat')
force=map(lambda x:x.id(),nodeFor[0].values())

nnodes    = len(nodes)
ndofs     = nnodes*3
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
Fglob  = zeros((ndofs,),'d')
Kglob  = zeros((ndofs,ndofs),'d')
valeff = ones((len(efforts),))*1000.
Fglob[efforts] = valeff
tdeb   = time.time()
print('....Debut d assemblage')
for el in els:
      el.setMaterialProperties(E,nu)
      el.setGaussPointsAndWeights(GP2,WP2)
      kel   = el.stiffness()
      ddls  = el.ddls()
      Kglob = assembMatrix(Kglob,kel,ddls)
print('....Fin d assemblage')

for do in encastre:
    Kglob[do,:]  = 0.
    Kglob[do,do] = 1.

print('....Resolution:K.u=F')
du= linalg.solve(Kglob,Fglob)
Du = zeros((nnodes,3),'d')
for i,ddl in enumerate(du[:ndofs]):
    node,comp      = nodeDdlNumber(i)
    Du[node,comp]  = ddl
    
sigmas  = []
for el in els:
     ddls = el.ddls()
     sigmas.append(el.computeStressesInElement(du[ddls]))
print('------Resolution en:',time.time()-tdeb,' s')
print('....Ecriture des resultats')
resFile = resultsFile("test.vtu")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
resFile.addVectorToCell(sigmas,'SIGM_ELNO')
resFile.write()
