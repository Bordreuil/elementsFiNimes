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

coords =array([[0.,0.],                    #0
               [L_barre/2.,L_barre],       #1
               [L_barre,0.],               #2
               [3.*L_barre/2.,L_barre],    #3
               [2.*L_barre,0.],            #4
               [5./2.*L_barre,L_barre],    #5
               [3*L_barre,0.]]   ,'d')     #6

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

plotElements(coords,els)
axis([-100,3.*L_barre+100,-100.,3.*L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)

Kglob = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')

F[5]  =  -5000                   #Chargement mecanique
F[9]  =  -5000                   #Chargement mecanique
imposedDofs      = [2 ,3 ,10,11] #Conditions limites
valuesImposed    = [0 ,0 ,0 ,0 ] #Conditions limites

print('\t\tNbre de ddls:',ndofs)

print('--------Assemblage des matrices de rigidite elementaires')

for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
for i,dof in enumerate(imposedDofs):
    Kglob[dof,:]=0.;Kglob[dof,dof]=1.;F[dof]=valuesImposed[i]

magnitude=500
print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)

du=solve(Kglob,F)                #Resolution des equations
Du[:,0]  = du[::2]
Du[:,1]  = du[1::2]

Coords     = coords+magnitude*Du

print('--------Visualisation de la deformee et des contraintes')

plotNodes(Coords)                #Traçage des deplacements de points de la structure
figure()

sigmas=[]
for el in els:                   #Calcul des contraintes
    ddls = el.ddls()
    sigma = el.calculContrainte(du[ddls])
    sigmas.append(sigma)
jet=get_cmap('jet')
plotContraintes(els,Coords,sigmas,jet)  #Traçage des contraintes
print('Valeur max de contrainte=',max(sigmas))
plotElements(coords,els)
show()
