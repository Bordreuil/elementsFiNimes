from barreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *
#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print '-------Definition du maillage'   
coords =array([[0.,0.],            # 0 ddl 0 et 1
               [0.,L_barre],         # 1 ddl 2 et 3
               [L_barre, 0.],        # 2 ddl 4 et 5
               [L_barre,L_barre],      # 3 ddl 6 et 7
               [2.*L_barre,0.],         # 4 ddl 8 et 9
               [2.*L_barre,L_barre],      # 5 ddl 10 et 11
               [3.*L_barre,0.],         # 6 ddl 12 et 13
               [3.*L_barre,L_barre]],'d') # 7 ddl 14 et 15

imposedDofs=[0,1,12,13]

ddlsActive = listActiveDofs(16,imposedDofs)

Du  = zeros(coords.shape,'d')

el1 = barre2D([0,1],L_barre,E,S,90.*pi/180.)
el2 = barre2D([0,2],L_barre,E,S,0.)
el3 = barre2D([0,3],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el4   = barre2D([1,3],L_barre,E,S,0.)
el5   = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el6   = barre2D([2,3],L_barre,E,S,90.*pi/180.)
el7   = barre2D([3,4],sqrt(2.)*L_barre,E,S,-45.*pi/180.)
el7b  = barre2D([2,5],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el8   = barre2D([3,5],L_barre,E,S,0.)
el9   = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el10  = barre2D([4,5],L_barre,E,S,90.*pi/180.)
el11  = barre2D([5,6],sqrt(2.)*L_barre,E,S,-45.*pi/180.)

el12  = barre2D([5,7],L_barre,E,S,0.*pi/180.)
el13  = barre2D([6,7],L_barre,E,S,90.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el7b,el8,el9,el10,el11,el12,el13]
print  '--------Definition du probleme global'
ndofs = getNumberOfDofs(coords)
print '\t\tNbre de ddls:',ndofs
K     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')
F[5] = -10000.
F[9] = -10000.
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
Coords     = coords+magnitude*Du
plotNodes(Coords)
sigmas     = []
print '--------Calcul des contraintes'
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)

jet   = get_cmap('jet')
print '--------Visualisation de la deformee et des contraintes'
plotContraintes(els,Coords,sigmas,jet)

show()
