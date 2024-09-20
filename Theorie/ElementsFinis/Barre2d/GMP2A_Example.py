import sys
sys.path.append('.')
from barreElement2d import *
from elementsTools  import *
from matrixTools    import *
#from visuTools      import * # Vous decommentez cette ligne si matplotlib est installe
#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print('-------Definition du maillage')
alpha  = 30.*pi/180.
coords = array([[0.,0.],                                                   # 0 
               [L_barre*(1.-cos(alpha)), L_barre*sin(alpha)],             # 1
               [L_barre*(1.-cos(2.*alpha)), L_barre*sin(2.*alpha)],       # 2
               [L_barre,L_barre],                                         # 3
               [L_barre,0.],],'d')                                        # 4
print(coords)
Du  = zeros(coords.shape,'d')

el1 = barre2D([0,4], L_barre,E,S,0.)
el2 = barre2D([1,4], L_barre,E,S,-30.*pi/180.)
el3 = barre2D([2,4], L_barre,E,S,-60.*pi/180.)
el4 = barre2D([3,4], L_barre,E,S,-90.*pi/180.)



els=[el1,el2,el3,el4]
# Si vous avez installe matplotlib vous pouvez decommenter (enlever le #) sur les lignes suivante 
#figure()
#plotElements(coords,els)
print('--------Definition du probleme global')
ndofs       = getNumberOfDofs(coords)
dofsImposed = [0,1,2,3,4,5,6,7]
ddlsActifs  = listActiveDofs(ndofs,dofsImposed)
print(ddlsActifs)
print('\t\tNbre de ddls:',ndofs)
K     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[ndofs-2] =10000.*sin(alpha)
F[ndofs-1] =-10000.*cos(alpha)

print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    K    = assembMatrix(K,k,ddls)
    
#printMatrix(K[4:,4:])

print('--------Resolution')
Ksolv = sliceMatrix(K,ddlsActifs,ddlsActifs)
du = linalg.solve(Ksolv,F[8:])
print(du)
Du[4,0]  = du[::2]
Du[4,1]  = du[1::2]
print(Du)
Duf       = Du.flatten()
magnitude = 10
print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
Coords     = coords+magnitude*Du

sigmas=[]
print('--------Calcul des contraintes')
for el in els:
    ddls  = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)


print('--------Visualisation de la deformee et des contraintes')
# idem si vous avez matplotlib
#figure()
#plotNodes(Coords)
#jet   = get_cmap('jet')
#plotContraintes(els,Coords,sigmas,jet)
#axis([-100,3500,-1600.,2000.])
#show()
