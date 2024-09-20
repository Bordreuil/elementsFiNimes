import sys
sys.path.append('..')
from barreElement2d import *
from matrixTools    import *
from visuTools      import *


#  Resolution d un probleme de structure treillis


#1) Caractéristique géométrique et surface des barres
L_barre = 1000.          # mm
E       = 200000.        # MPa
S       = 200.           # mm**2
Force   = 5000.          # N
A       = -30.*pi/180    # °

#2) Numérotation des noeuds et des éléments
coords =array([[0.,0.],                       #0
               [0.,L_barre],                  #1
               [L_barre,0.],                  #2
               [L_barre,L_barre],             #3
               [2.*L_barre,0.],               #4
               [2.*L_barre,L_barre],          #5
               [3.*L_barre,0.],               #6
               [3.*L_barre,L_barre]]   ,'d')  #7

#3) Application des inconnues de liaison
imposedDofs    = [0,1,2,3,7]
valuesImposed  = [0.,0.,0.,0.,0.]


#Rentrer le nombre d'inconnues
ddlsActive = listActiveDofs(16,imposedDofs)
print('Taille de coords:',coords.shape)
print('ddls actifs :', ddlsActive)
Du  = zeros(coords.shape,'d')

#2) Création des différentes barres

s2 = sqrt(2.)
el1 = barre2D([0,1],L_barre,E,S,90.*pi/180.)
el2 = barre2D([0,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([0,3],s2*L_barre,E,S,45.*pi/180.)
el4 = barre2D([1,3],L_barre,E,S,0.*pi/180.)
el5 = barre2D([2,3],L_barre,E,S,90.*pi/180.)
el6 = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el7 = barre2D([3,4],s2*L_barre,E,S,-45.*pi/180.)
el8 = barre2D([4,5],L_barre,E,S,90.*pi/180.)
el9 = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el10 = barre2D([5,6],s2*L_barre,E,S,-45.*pi/180.)
el11 = barre2D([4,7],s2*L_barre,E,S,45.*pi/180.)
el12 = barre2D([6,7],L_barre,E,S,90.*pi/180.)
el13 = barre2D([5,7],L_barre,E,S,0.*pi/180.)
el14 = barre2D([3,5],L_barre,E,S,0.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13,el14]


#Création de la matrice avec le nombre d'inconnu de déplacement
Kglob     = zeros((16,16),'d')
F         = zeros((16,),'d')

#3) Application des forces exercées sur les noeuds
print('Valeur des Forces exercées en chaque noeud:')
F[12]      = Force*cos(A)
F[13]      = Force*sin(A)
print('Fx1:', F[12])
print('Fy1:', F[13])
input('?')
figure()


print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)

#Définition de la zone d'impression Figure 1
plot(coords[:,0],coords[:,1],'o')
axis([-L_barre/2,L_barre*5,-L_barre/2,3*L_barre/2])


#Application des conditions aux différents noeuds
Kdep = Kglob.copy()
for i, dof in enumerate(imposedDofs):
    Kglob[dof,:]=0.;Kglob[dof,dof]=1.;F[dof]=valuesImposed[i]

#4) Résolution du problème et affichage du déplacement en chaque noeud
print('------Resolution')
du=solve(Kglob,F)
print('debut:',Du,du)
Du[:,0]  = du[::2]
print('apres:',Du)
Du[:,1]  = du[1::2]
print('fin:',Du)
Duf  = Du.flatten()
print('Déplacement à plat:',Duf)

#5) Affichage du déplacement maximal et donc du noeud correspondant
print('Déplacement maximal:', max(Duf))
input('?')
print('Effort de liaison:', dot(Kdep,Duf)[:4])
magnitude = 100.
print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
print(Du)
Coords     = coords+magnitude*Du

# Affichage des nouveaux points de la déformée
plot(Coords[:,0],Coords[:,1],'o')
show()
sigmas=[]

#6) Calcul des contraintes
print('--------Calcul des contraintes')
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
figure()
plotNodes(Coords)
masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
jet   = get_cmap('jet')

#7) Observation de la barre la plus chargée
print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)

#Vérification par visualisation de la Figure 2
print('--------Visualisation de la deformee et des contraintes')
for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)


# Définition de la zone d'impression Figure 2
plotContraintes(els,Coords,sigmas,jet)
axis([-L_barre/2,L_barre*5,-L_barre/2,3*L_barre/2])
show()
