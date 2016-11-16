from element2d   import *
from readGmsh    import *
from pointsGauss import *
from matrixTools import *
from visuTools   import *

E  = 200000.
nu = 0.3

nodes,els  = readGmsh('datas/plaque.msh')
nnodes     = len(nodes)
ndofs      = nnodes*2

nodesBas  = [ 0 , 1 , 4 , 5, 6 , 7, 8, 9, 10,11 ,12]
nodesHaut = [ 2,3,52,53,54,55,56,57,58,59,60]

encastre=[]
for i in nodesBas:
    encastre.append(dofNumberGlobal(i,0))
    encastre.append(dofNumberGlobal(i,1))

efforts=[]
for i in nodesHaut:
    efforts.append(dofNumberGlobal(i,1))
values =zeros((len(encastre),),'d')
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

Du = zeros((nnodes,2),'d')
Du[:,0] = du[::2]
Du[:,1] = du[1::2]

resFile = resultsFile("test.vtp")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
resFile.write()

