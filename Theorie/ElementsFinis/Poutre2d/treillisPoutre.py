from poutreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *
#  Resolution d un probleme de structure treillis

L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2
b       = 20.     # mm
h       = 20.     #mm 
bi      = 16      # mm
hi      = 16      # mm
I       = b**3*h/12-bi**3*hi/12
print '-------Definition du maillage'   
coords =array([[0.,0.],            # 0 ddl 0 1 2
               [0.,L_barre],         # 1 ddl 3 4 5
               [L_barre, 0.],        # 2 ddl 6 7 8
               [L_barre,L_barre],      # 3 ddl 9 10 11
               [2.*L_barre,0.],         # 4 ddl 12 13 14
               [2.*L_barre,L_barre],      # 5 ddl 15 16 17
               [3.*L_barre,0.],         # 6 ddl 18 19 20
               [3.*L_barre,L_barre]],'d') # 7 ddl 21 22 23

imposedDofs=[0,1,18,19]

ddlsActive = listActiveDofs(24,imposedDofs)

Du  = zeros((coords.shape[0],3),'d')

el1 = poutre2D([0,1],L_barre,E,S,I,90.*pi/180.)
el2 = poutre2D([0,2],L_barre,E,S,I,0.)
el3 = poutre2D([0,3],sqrt(2.)*L_barre,E,S,I,45.*pi/180.)

el4   = poutre2D([1,3],L_barre,E,S,I,0.)
el5   = poutre2D([2,4],L_barre,E,S,I,0.*pi/180.)
el6   = poutre2D([2,3],L_barre,E,S,I,90.*pi/180.)
el7   = poutre2D([3,4],sqrt(2.)*L_barre,E,S,I,-45.*pi/180.)
el7b  = poutre2D([2,5],sqrt(2.)*L_barre,E,S,I,45.*pi/180.)

el8   = poutre2D([3,5],L_barre,E,S,I,0.)
el9   = poutre2D([4,6],L_barre,E,S,I,0.*pi/180.)
el10  = poutre2D([4,5],L_barre,E,S,I,90.*pi/180.)
el11  = poutre2D([5,6],sqrt(2.)*L_barre,E,S,I,-45.*pi/180.)

el12  = poutre2D([5,7],L_barre,E,S,I,0.*pi/180.)
el13  = poutre2D([6,7],L_barre,E,S,I,90.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el7b,el8,el9,el10,el11,el12,el13]
print  '--------Definition du probleme global'
ndofs = getNumberOfDofs(coords)
print '\t\tNbre de ddls:',ndofs
K     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[7] = -10000.
F[13] = -10000.
figure()

print '--------Assemblage des matrices de rigidite elementaires'
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    K    = assembMatrix(K,k,ddls)

#printMatrix(K[4:,4:])
axis([-100,3500,-1600.,2000.])

print '--------Resolution'

Kprob = sliceMatrix(K,ddlsActive,ddlsActive)

du    = solve(Kprob,F[ddlsActive])

print '--------Affectation des ddls globaux'
for i,ddl in enumerate(ddlsActive):
    node,comp = nodeDdlNumber(ddl)
    Du[node,comp]  = du[i]
    
Duf  = Du.flatten()
magnitude = 300.

print '--------Calcul des coordonnes deforme avec une magniture de:',magnitude
Coords     = coords+magnitude*Du[:,:2]
plotNodes(Coords)
plotElements(Coords,els)
sigmas     = []
print '--------Calcul des contraintes'
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainteTraction(Duf[ddls])
    sigmas.append(sigma)

jet   = get_cmap('jet')
print '--------Visualisation de la deformee et des contraintes de traction'
plotContraintes(els,Coords,sigmas,jet)

show()
