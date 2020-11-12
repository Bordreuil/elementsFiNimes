from element2d   import *
from readGmsh    import *
from pointsGauss import *
from matrixTools import *
from visuTools   import *

E  = 200000.
nu = 0.3
#lecture du maillage
print('.....Lecture du maillage')
nodes,els  = readGmsh('datas/plaquetrouee.msh')
nnodes     = len(nodes)
ndofs      = nnodes*2
print('.....Definition des conditions aux limites')
#print 'Nombre total de degre de liberte:',ndofs
nodesBas  = [ 0 , 1 , 4, 6  , 7, 8, 9, 10,11 ,12,13,14]
nodesHaut = [ 2,3,54,55,56,57,58,59,60,61,62]

encastre=[]
for i in nodesBas:
    encastre.append(dofNumberGlobal(i,0))
    encastre.append(dofNumberGlobal(i,1))

efforts=[]
for i in nodesHaut:
    efforts.append(dofNumberGlobal(i,1))
values =zeros((len(encastre),),'d')
#print '....Nbre de noeuds\t:',len(nodes)
#print '....Nbre de ddls\t:',ndofs

Kglob=zeros((ndofs,ndofs),'d')
Fglob=zeros((ndofs,),'d')
Fglob[efforts]=1000.
print('.....Calcul des matrices elementaires et assemblage')
for el in els:
    el.setMaterialProperties(E,nu)
    el.setGaussPointsAndWeights(GP1,WP1)
    kel   = el.stiffness()
    ddls  = el.ddls()
    Kglob = assembMatrix(Kglob,kel,ddls)
    
Kprob,Fprob = imposedDofsOnMatrixAndRhs(Kglob,Fglob,encastre,values)
print('.....Resolution [K].u=F')
du=linalg.solve(Kprob,Fprob)

Du = zeros((nnodes,2),'d')
Du[:,0] = du[::2]
Du[:,1] = du[1::2]
sigmas  = []
print('.....Calcul des contraintes dans les elements')
for el in els:
    ddls = el.ddls()
    sigmas.append(el.computeStressesInElement(du[ddls]))

print('.....Impression des resultats')
resFile = resultsFile("plaquetroueeGP1WP1.vtp")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
resFile.addVectorToCell(sigmas,'SIGM_ELNO')
resFile.write()

