import sys
sys.path.append('..')
from barreElement2d import *
from matrixTools    import *
from visuTools      import *

#  Resolution d un probleme de structure treillis

L_barre = 1000.     # mm
E       = 200000.   # MPa
S       = 200.      # mm**2

# Définition des noeuds
coords =array([[0.,0.],                     # 0
               [2.*L_barre,0.],             # 1
               [3.*L_barre,0.],             # 2
               [2.*L_barre,L_barre],        # 3
               [0.,2.*L_barre],             # 4
               [2.*L_barre,2.*L_barre],     # 5
               [3.*L_barre,2.*L_barre],     # 6
               [5.*L_barre,L_barre]],'d')   # 7


# Definition des appuis
ImposedDofs = [5,6,13,15,16]                 # Rang du vecteur
valuesImposed = [0.,0.,0.,0.,0.]


#8 noeuds * 2 ddls = 16 ddls
ddlsActive = listActiveDofs(16,ImposedDofs)
print('ddls actifs:',ddlsActive)
Du  = zeros(coords.shape,'d')

# Définition des barres
el1 = barre2D([0,1],2.*L_barre,E,S,0.*pi/180.)
el2 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([0,5],sqrt(2.)*2.*L_barre,E,S,45.*pi/180.)
el4 = barre2D([0,4],L_barre,E,S,90.*pi/180.)
el5 = barre2D([4,5],2.*L_barre,E,S,0.*pi/180.)
el6 = barre2D([5,6],L_barre,E,S,0.*pi/180.)
el7 = barre2D([1,3],L_barre,E,S,90.*pi/180.)
el8 = barre2D([3,5],L_barre,E,S,90.*pi/180.)
el9 = barre2D([2,3],sqrt(2.)*L_barre,E,S,135.*pi/180.)
el10 = barre2D([3,6],sqrt(2.)*L_barre,E,S,45.*pi/180.)
el11 = barre2D([2,6],2.*L_barre,E,S,90.*pi/180.)
el12 = barre2D([6,7],sqrt(5.)*L_barre,E,S,-63.*pi/180.)
el13 = barre2D([2,7],sqrt(5.)*L_barre,E,S,63.*pi/180.)

els = [el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13]

K= zeros((16,16),'d')
F = zeros((16,),'d')

# Definition des forces exterieures
F[9] =5196.
F[10] =-3000.

print('----------Assemblage des matrices de rigidite elementaires')

for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    K=assembMatrix(K,k,ddls)
    print('Matrice globale:',K)

Kglob = K.copy()
Kprob = sliceMatrix(K,ddlsActive,ddlsActive)

du = linalg.solve(Kprob,F[ddlsActive])
print(nodeDdlNumber(5))

print('----------Affectation des ddls globaux')

for i,dof in enumerate(ImposedDofs):
    Kglob[dof,:] = 0.;Kglob[dof,dof]=1.;F[dof] = valuesImposed[i]

print('----------Resolution')

du = solve(Kglob,F)
print('debut',Du,du)
Du[:,0] = du[::2]
print('apres',Du)
Du[:,1] = du[1::2]
print('fin')
Duf = Du.flatten()
print(Duf)
magnitude = 100.

plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-1600.,2000.])

print('----------Calcul des coordonnes deforme avec une magnitude de:',magnitude)
print(Du)

Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
figure()
sigmas=[]
print('Calcul des contraintes')
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
figure()
plotNodes(Coords)
jet   = get_cmap('jet')

print('----------Visualisation de la deformee et des contraintes')
plotContraintes(els,Coords,sigmas,jet)
show()
