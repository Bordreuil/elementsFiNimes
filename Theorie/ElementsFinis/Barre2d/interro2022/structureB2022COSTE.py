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
               [L_barre, 0.],
               [2*L_barre,0],
               [0.,L_barre],
               [L_barre,L_barre],
               [L_barre,2.*L_barre]]   ,'d')

dofsImposed = [ 6,7 ,10 ,11]
valsImposed = [0.,0.,0.,0.]

Du  = zeros(coords.shape,'d')


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
plotElements(coords,els)
axis([-100-sqrt(3.)*L_barre/2.,2.*L_barre+100,-100.,2.*L_barre+100.])
print ('--------Definition du probleme global')
ndofs = getNumberOfDofs(coords)

print('\t\tNbre de ddls:',ndofs)
Kglob = zeros((ndofs, ndofs),'d')
F     = zeros((ndofs,),'d')
F[3] = -1750
F[5] = -3500

print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)


print('--------Imposition des deplacements imposes')

KglobNonModif = Kglob.copy()

for i,dof in enumerate(dofsImposed):
            print(i,dof,valsImposed[i])
            Kglob[dof,:] = 0.;Kglob[dof,dof]= 1.;F[dof] = valsImposed[i]

print('--------Resolution')
du=solve(Kglob,F)

print('--Calcul de la force sur le noeud 0 suivant Y')
Y = dot(KglobNonModif[1,:],du)
print('Effort y0 :',Y,'N')

Du[:,0]  = du[::2]  #deplacement suivant x
Du[:,1]  = du[1::2] #deplacement suivant y
Duf       = Du.flatten()
print(Duf)
magnitude = 100.


print('--------Calcul des coordonnes deforme avec une magniture de:')
print(Du)
Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()

print('--------Calcul des contraintes')
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

print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)

print('--------Visualisation de la deformee et des contraintes')
figure()
for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)

axis([-100,3.*L_barre+100,-100.,2.*L_barre+100.])

plotContraintes(els,Coords,sigmas,jet)
plotElements(coords,els)
show()
