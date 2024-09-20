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
coords =array([[0.,0.],
               [0.,L_barre],
               [L_barre, 0.],
               [L_barre,L_barre],
               [2.*L_barre,0.],
               [2.*L_barre,L_barre],
               [3.*L_barre,0.],
               [3.*L_barre,L_barre]],'d')

imposedDofs=[2,3,14,15]
valuesImposed=[0,0,0,0]
print('Taille de coords:',coords.shape)
Du  = zeros(coords.shape,'d')

el1 = barre2D([0,1],L_barre,E,S,90.*pi/180.)
el2 = barre2D([0,2],L_barre,E,S,0.)
el3 = barre2D([0,3],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el4   = barre2D([1,3],L_barre,E,S,0.)
el5   = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el6   = barre2D([2,3],L_barre,E,S,90.*pi/180.)
el7   = barre2D([3,4],sqrt(2.)*L_barre,E,S,-45.*pi/180.)
el8  = barre2D([2,5],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el9   = barre2D([3,5],L_barre,E,S,0.)
el10   = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el11  = barre2D([4,5],L_barre,E,S,90.*pi/180.)
el12  = barre2D([5,6],sqrt(2.)*L_barre,E,S,-45.*pi/180.)

el13  = barre2D([5,7],L_barre,E,S,0.*pi/180.)
el14  = barre2D([6,7],L_barre,E,S,90.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13,el14]
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)
print('--------Nbre de ddls:',ndofs)
Kglob = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[6]  =-7500. # on met -7500 N sur v3
F[10] =-7500. # on met -7500 N sur v5
figure()

print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)

    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)
plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-1600.,2000.])

print('--------Imposition des deplacements imposes')

for i,dof in enumerate(imposedDofs):
    Kglob[dof,:]=0;Kglob[dof,dof]=1;F[dof]=valuesImposed[i]

print('--------Resolution')
Kdep=Kglob.copy() # On copie K

print('--------Affectation des ddls globaux')
du=solve(Kglob,F) #résolution de l'équation pour trouver du
print('debut:',Du,du)
Du[:,0]  = du[::2] # on remplie Du que avec les u (de deux en deux en partant de 0)
print('apres:',Du)
Du[:,1]  = du[1::2] # on remplie Du que avec les v (de deux en deux en partant de 1)
print('fin:',Du)
Duf       = Du.flatten()
print('déplacement a plat',Duf)
print('Effort de liaison',dot(Kdep,Duf)[:2]) # on calcule les effort de laision
print('Effort de liaison',dot(Kdep,Duf)[-2:]) # on calcule les effort de laision
magnitude = 100.

print('--------Calcul des coordonnes deforme avec une magniture de:100')
print(Du)
Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
figure('contraintes')
sigmas=[]

print('--------Calcul des contraintes')
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
plotNodes(Coords)
jet   = get_cmap('jet')
print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)

print('--------Visualisation de la deformee et des contraintes')
title('contraintes')
plotElements(coords,els)
show()
