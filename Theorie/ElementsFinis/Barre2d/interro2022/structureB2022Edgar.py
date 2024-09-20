import sys
sys.path.append('..')
from barreElement2d import *
from matrixTools    import *
from visuTools      import *

#  Resolution d un probleme de structure treillis
plotUndistord = False
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

print('-------Definition du maillage')
coords =array([[0.,0.],                        #0
               [L_barre, 0.],                  #1
               [2*L_barre,0],                  #2
               [0.,L_barre],                   #3
               [L_barre,L_barre],              #4
               [L_barre,2.*L_barre]]   ,'d')   #5

Du  = zeros(coords.shape,'d')

#liaisons imposées aux noeuds
imposedDofs    = [4,5,10,11]
valuesImposed  = [0.,0.,0.,0.]

# 6 noeuds x 2 ddl = 12 ddls
ddlsActive = listActiveDofs(12,imposedDofs)
print('Taille de coords:',coords.shape)
print('ddls actifs :', ddlsActive)
print('Taille de coords:',coords.shape)
Du  = zeros(coords.shape,'d')

# definition des barres

el1 = barre2D([0,1],L_barre,E,S,0.*pi/180.)
el2 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([0,3],L_barre,E,S,90.*pi/180.)

el4 = barre2D([1,3],sqrt(2.)*L_barre,E,S,135.*pi/180.)
el5 = barre2D([3,4],L_barre,E,S,0.*pi/180.)
el6 = barre2D([1,4],L_barre,E,S,90*pi/180.)
el7 = barre2D([2,4],sqrt(2.)*L_barre,E,S,135*pi/180.)
el8 = barre2D([3,5],sqrt(2.)*L_barre,E,S,45.*pi/180.)
el9 = barre2D([4,5],L_barre,E,S,0.*pi/180.)
el10 = barre2D([2,5],sqrt(5.)*L_barre,E,S,116.*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10]

Kglob     = zeros((12,12),'d')
F     = zeros((12,),'d')

F[0] =-5000
F[1] =-5000

figure() #pour moi pour regarder la figure

# plotElements(coords,els)
# axis([-100-sqrt(3.)*L_barre/2.,2.*L_barre+100,-100.,2.*L_barre+100.])
# print ('--------Definition du probleme global')
# ndofs = getNumberOfDofs(coords)

for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)

plot(coords[:,0],coords[:,1],'o')
axis([-100,2500,-100.,2500.])

print('--------Resolution')

Kdep = Kglob.copy()
Kprob = sliceMatrix(Kglob, ddlsActive, ddlsActive)
du=solve(Kprob,F[ddlsActive])

for i, ddl in enumerate(ddlsActive):
    node,comp = nodeDdlNumber(ddl)
    Du[node,comp] = du[i]
Duf       = Du.flatten()

print('Déplacement à plat:',Duf)

print('Effort de liaison:', dot(Kdep,Duf)[:4])

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

print('--Visualisation de la déformée et des contraintes')

plotContraintes(els, Coords, sigmas, jet)
show()

masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
jet   = get_cmap('jet')

print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)


for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)


axis([-100,2500,-100.,2500.])



show()

plotElements(coords,els)
show()
