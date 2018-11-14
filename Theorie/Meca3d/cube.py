from readDat     import *
from element3d   import *
from pointsGauss import *
from matrixTools import *
from visuTools   import *

E         = 200000.
nu        = 0.3

nodes,els = readDat('datas/tesUn.dat')


nnodes     = len(nodes)
ndofs      = nnodes*3

nodesBas  = [0,1,2,3]
nodesHaut = [4,5,6,7]

encastre  = []
encastre.append(dofNumberGlobal(0,0))
encastre.append(dofNumberGlobal(0,1))
encastre.append(dofNumberGlobal(0,2))
encastre.append(dofNumberGlobal(1,0))
encastre.append(dofNumberGlobal(1,1))
encastre.append(dofNumberGlobal(2,0))
encastre.append(dofNumberGlobal(2,2))
encastre.append(dofNumberGlobal(3,0))


efforts=[]
for i in nodesHaut:
    efforts.append(dofNumberGlobal(i,0))
print encastre
print efforts
values = zeros((len(encastre),),'d')
print '....Nbre de noeuds\t:',len(nodes)
print '....Nbre de ddls\t:',ndofs

Kglob=zeros((ndofs,ndofs),'d')
Fglob=zeros((ndofs,),'d')
Fglob[efforts]=1000.

for el in els:
    el.setMaterialProperties(E,nu)
    el.setGaussPointsAndWeights(GP2,WP2)
    kel   = el.stiffness()
    ddls  = el.ddls()
    Kglob = assembMatrix(Kglob,kel,ddls)
    
Kprob,Fprob = imposedDofsOnMatrixAndRhs(Kglob,Fglob,encastre,values)

du=linalg.solve(Kprob,Fprob)

Du = zeros((nnodes,3),'d')
Du[:,0] = du[::3]
Du[:,1] = du[1::3]
Du[:,2] = du[2::3]
print Du
# sigmas  = []
# for el in els:
#     ddls = el.ddls()
#     sigmas.append(el.computeStressesInElement(du[ddls]))


resFile = resultsFile("test.vtu")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
#resFile.addVectorToCell(sigmas,'SIGM_ELNO')
resFile.write()
