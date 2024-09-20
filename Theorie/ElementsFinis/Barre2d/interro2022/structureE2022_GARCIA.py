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

coords =array([[0.,0.],               #0
               [0.,L_barre],          #1
               [L_barre,0.],          #2
               [L_barre,L_barre],     #3
               [2.*L_barre,0.],       #4
               [2.*L_barre,L_barre],  #5
               [3.*L_barre,0.],       #6
               [3.*L_barre,L_barre]]   ,'d')   #7

Du  = zeros(coords.shape,'d')

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

plotElements(coords,els)
axis([-100,3.*L_barre+100,-100.,L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)
Kglob     = zeros((16,16),'d')
F     = zeros((16,),'d')
F[2] =-6000.

print('\t\tNbre de ddls:',ndofs)

print('--------Assemblage des matrices de rigidite elementaires')

for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)

print('--------Resolution')

du=solve(Kglob[:11,:11],F[:11])
print('debut:',Du,du)
Du[0,:11]  = du[::11]
print('apres:',Du)
Du[0,:11]  = du[0::11]
print('fin:',Du)
Duf       = Du.flatten()
print(Duf)
magnitude = 100.

print('--------Calcul des coordonnes deforme avec une magnitude de:')

Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
sigmas=[]

for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
print(sigmas)
masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
jet   = get_cmap('jet')

print('--------Visualisation de la deformee et des contraintes')

for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)

axis([-100,3500,-1600.,2000.])

show()
