import sys
sys.path.append('..')
from barreElement2d import *
from elementsTools   import *
from matrixTools    import *
from visuTools      import *

#  Resolution d un probleme de structure treillis
plotUndistord = False

# Caractéristiques des barres
L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2
Force   = 10000.   # N

print('-------Definition du maillage')

#Définition des noeuds :
coords =array([[0.,0.],                   #0
               [L_barre/2.,L_barre],      #1
               [L_barre,0.],              #2
               [3.*L_barre/2.,L_barre],   #3
               [2.*L_barre,0.],           #♥4
               [5./2.*L_barre,L_barre],   #5
               [3*L_barre,0.]]   ,'d')    #6


#Affectation des inconnues de liaison
dofsImposed    = [6,7,8,9]
valuesImposed  = [0.,0.,0.,0.]


#Nombre d'inconnues :
# 7 noeuds x 2 ddl = 14 ddls
ddlsActive = listActiveDofs(14,dofsImposed)
print('Taille de coords:',coords.shape)
print('ddls actifs :', ddlsActive)
Du  = zeros(coords.shape,'d')



#Affectation des barres :
Du  = zeros(coords.shape,'d')
alpha = 63.
s3 = sqrt(3.)/2.
el1 = barre2D([0,1],s3*L_barre,E,S,alpha*pi/180.)
el2 = barre2D([0,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([1,2],s3*L_barre,E,S,-alpha*pi/180.)
el4 = barre2D([1,3],L_barre,E,S,0.*pi/180.)
el5 = barre2D([2,3],s3*L_barre,E,S,alpha*pi/180.)
el6 = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el7 = barre2D([3,4],s3*L_barre,E,S,-alpha*pi/180.)
el8 = barre2D([3,5],L_barre,E,S,0.)
el9 = barre2D([4,5],s3*L_barre,E,S,alpha*pi/180.)
el10 = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el11 = barre2D([5,6],s3*L_barre,E,S,-alpha*pi/180.)

els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11]




#Création de la matrice :
Kglob     = zeros((14,14),'d')
F     = zeros((14,),'d')
F[0] =-Force*sin(30)  #N
F[1] =-Force*cos(30)  #N
figure()


print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    Kglob=assembMatrix(Kglob,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)


#Changer les axes : (figure 1)

plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-100.,1500.])


#show()
#print('--------Resolution')
Kdep = Kglob.copy()
for i, dof in enumerate(dofsImposed):
    Kglob[dof,:]=0.;Kglob[dof,dof]=1.;F[dof]=valuesImposed[i]


print('--------Resolution')
du=solve(Kglob,F)
print('debut:',Du,du)
Du[:,0]  = du[::2]
print('apres:',Du)
Du[:,1]  = du[1::2]
print('fin:',Du)
Duf  = Du.flatten()

#Définir les déplacements :
print('Déplacement à plat:',Duf)
print('Effort de liaison:', dot(Kdep,Duf)[:4])
magnitude = 100.

#Déinir le deplacement max :
print('Déplacement max:', max(Duf))
input('?')




print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
print(Du)
Coords     = coords+magnitude*Du

#Affichages Noeuds qui ont bougés :
plot(Coords[:,0],Coords[:,1],'o')
show()
sigmas=[]


#Calcul des contraintes :
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


#Contrainte maxi :
print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)
print('--------Visualisation de la deformee et des contraintes')

for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)

#Axes figure 2 :
axis([-100,3500,-1600.,2000.])

plotContraintes(els,Coords,sigmas,jet)
show()

print('Merci pour tout M.Bordreuil!!!!!!!!!!!!!!!!!')
print('Signé : La cluche')


