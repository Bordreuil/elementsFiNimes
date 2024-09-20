import sys
sys.path.append('..')
from barreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *
#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print('-------Definition du maillage')

coords =array([[0.,0.],  # 0 ddl 0 et 1
               [L_barre/2.,L_barre],     # 1 ddl 2 et 3
               [L_barre,0.],     # 2 ddl 4 et 5
               [3.*L_barre/2.,L_barre],  # 3 ddl 6 et 7
               [2.*L_barre,0.],  # 4 ddl 8 et 9
               [5./2.*L_barre,L_barre],  # 5 ddl 10 et 11
               [3*L_barre,0.]]   ,'d')   # 6 ddl 12 et 13

imposedDofs=[4,5,8,9]
valuesImposed = [0 , 0 , 0 ,  0 ]
#7 noeuds  x 2ddl = 14 ddls
ddlsActive = listActiveDofs(14,imposedDofs)
print('Taille de coords:',coords.shape)
print('ddls actifs :',ddlsActive)

Du  = zeros(coords.shape,'d')
alpha = 63.
s3 = sqrt(3.)/2.
el1 = barre2D([0,1],s3*L_barre,E,S,alpha*pi/180.)
el2 = barre2D([0,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([1,2],s3*L_barre,E,S,-alpha*pi/180.)
el4 = barre2D([1,3],L_barre,E,S,0.*pi/180.)
el5 = barre2D([2,3],s3*L_barre,E,S,alpha*pi/180.)
el6 = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el7 = barre2D([3,4],s3*L_barre,E,S,-alpha*pi/180.)
el8 = barre2D([3,5],L_barre,E,S,0.)
el9 = barre2D([4,5],s3*L_barre,E,S,alpha*pi/180.)
el10 = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el11 = barre2D([5,6],s3*L_barre,E,S,-alpha*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11]

ndofs = 14
Kglob     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')

figure()
ndofs = 16
Kglob     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[0] =-5000.
F[1] =10000.*sin(60.)
F[12] = 5000.
F[13] = 10000.*sin(60)
figure()



print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)
#printMatrix(K[4:,4:])
plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-1600.,2000.])
#show()
Kdep= Kglob.copy()

print('-----------Imposition des deoplacements imposes')
for i,dof in enumerate(imposedDofs):
    Kglob[dof,:] = 0.;Kglob[dof,dof]=1.;F[dof]= valuesImposed[i]
print(Kglob)
ok = input('?')

print('--------Resolution')

Kprob = sliceMatrix(Kglob,ddlsActive,ddlsActive)

du= linalg.solve(Kprob,F[ddlsActive])

print(nodeDdlNumber(5))

print('----------Affectation des ddls globaux')

for i,ddl in enumerate(ddlsActive):
    node,comp = nodeDdlNumber(ddl)
    Du[node,comp] = du[i]

Duf = Du.flatten()

print('valeur deplacement',Du[2,1],Du[4,1])

ok = input('?')



# #print('debut:',Du,du)
# Du[2:,0]  = du[::2]
# print('apres:',Du)
# Du[2:,1]  = du[1::2]
# print('fin:',Du)
# Duf       = Du.flatten()
# print(Duf)
#print('Effort de liaison:',dot(Kdep,Duf)[:4])
ok = input('?')
magnitude = 100.
print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
print(Du)
Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
sigmas=[]
print('--------Calcul des contraintes')
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
figure()
plotNodes(Coords)
jet = get_cmap('jet')
print('--------------Visualisation de la deformee et des contraintes')
plotContraintes(els,Coords,sigmas,jet)
axis([-100,3500,-1600.,2000.])
show()
