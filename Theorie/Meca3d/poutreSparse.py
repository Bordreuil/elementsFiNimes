from readDat     import *
from element3d   import *
from pointsGauss import *
from matrixTools import *
from elementsTools import *
from visuTools   import *
from scipy.sparse import *
from scipy.sparse.linalg import spsolve
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
Fglob = zeros((ndofs,),'d')

valeff = ones((len(efforts),))*1000.
Fglob[efforts] = valeff
tdeb=time.time()
datas       = {}
for el in els:
    for ddlc in el.ddls():
        for ddl in el.ddls():
            datas[(ddlc,ddl)]  = 0.
    

# print('....Debut d assemblage')
for el in els:
       el.setMaterialProperties(E,nu)
       el.setGaussPointsAndWeights(GP2,WP2)
       kel   = el.stiffness()
       ddls  = el.ddls()
#       #Kglob.setValues(ddls,ddls,kel,PETSc.InsertMode.ADD)
#       #Kglob = assembMatrix(Kglob,kel,ddls)
       for i,ido in enumerate(ddls):
           for j,idc in enumerate(ddls):
               datas[(ido,idc)]+=kel[i,j]
rows=[]
cols=[]
donnees = []
for ligne,col in datas.keys():
    rows.append(ligne)
    cols.append(col)
    if ligne in encastre:
        datas[(ligne,col)] = 0.
    if ligne in encastre and ligne== col:
        datas[(ligne,col)] = 1.
    donnees.append(datas[(ligne,col)])

Kglob = csr_matrix((donnees,(rows,cols)),(ndofs,ndofs))
print('....Fin d assemblage')
# for dof in encastre:
#     Kglob[dof,:]   = 0.
#     Kglob[dof,dof] = 1.
print('....Resolution:K.u=F')
du= spsolve(Kglob,Fglob)
Du = zeros((nnodes,3),'d')
for i,ddl in enumerate(du[:ndofs]):
     node,comp      = nodeDdlNumber(i)
     Du[node,comp]  = ddl
# # # print Du
sigmas  = []
for el in els:
     ddls = el.ddls()
     sigmas.append(el.computeStressesInElement(du[ddls]))
print('------Resolution en:',time.time()-tdeb,' s')
print('....Ecriture des resultats')
resFile = resultsFile("testSparse.vtu")
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(Du,'DEPL')
resFile.addVectorToCell(sigmas,'SIGM_ELNO')
resFile.write()
