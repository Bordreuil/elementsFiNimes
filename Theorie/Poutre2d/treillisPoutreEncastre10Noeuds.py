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
X      = arange(0,L_barre+L_barre/10.,L_barre/10.)

coords = zeros((X.shape[0],2),'d')
coords[:,0] = X
imposedDofs=[0,1,2]
ndofs = getNumberOfDofs(coords)
ddlsActive = listActiveDofs(ndofs,imposedDofs)
print ddlsActive
Du  = zeros((coords.shape[0],3),'d')
els = []
for i in range(coords.shape[0]-1):
    print 'Element connectivite:',i,i+1
    els.append(poutre2D([i,i+1],L_barre/10.,E,S,I,0.))
               
print  '--------Definition du probleme global'

print '\t\tNbre de ddls:',ndofs
K     = zeros((ndofs,ndofs),'d')
F     = zeros((ndofs,),'d')

F[ndofs-2] = -1000.

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
print du
for i,ddl in enumerate(ddlsActive):
    node,comp      = nodeDdlNumber(ddl)
    Du[node,comp]  = du[i]
    
Duf  = Du.flatten()
magnitude = 1.

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
