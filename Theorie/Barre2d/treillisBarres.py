from barreElement2d import *
from matrixTools    import *

#  Resolution d un probleme de structure treillis

L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2


coords =array([[0.,0.],            # 0 
               [0.,1000.],         # 1
               [1000., 0.],        # 2
               [1000.,1000.],      # 3
               [2000.,0.],         # 4
               [2000.,1000.],      # 5
               [3000.,0.],         # 6
               [3000.,1000.]],'d') # 7

Du  = zeros(coords.shape,'d')
el1 = barre2D([0,1],L_barre,E,S,0.)
el2 = barre2D([0,1],L_barre,E,S,90.*pi/180.)
el2b= barre2D([0,2],L_barre,E,S,0.)
el3 = barre2D([0,3],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el4 = barre2D([1,3],L_barre,E,S,0.)
el5 = barre2D([2,4],L_barre,E,S,0.*pi/180.)
el6 = barre2D([2,3],L_barre,E,S,90.*pi/180.)
el7 = barre2D([2,5],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el8  = barre2D([3,5],L_barre,E,S,0.)
el9  = barre2D([4,6],L_barre,E,S,0.*pi/180.)
el10 = barre2D([4,5],L_barre,E,S,90.*pi/180.)
el11  = barre2D([4,7],sqrt(2.)*L_barre,E,S,45.*pi/180.)

el12  = barre2D([5,7],L_barre,E,S,0.*pi/180.)
el13 = barre2D([6,7],L_barre,E,S,90.*pi/180.)

els=[el1,el2,el2b,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13]

K     = zeros((16,16),'d')
F     = zeros((16,),'d')
F[15] =-10000.
figure()
print '--------Assemblage des matrices de rigidite elementaires'
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    conn = el.connectivite()
    K=assembMatrix(K,k,ddls)
    plot(coords[conn,0],coords[conn,1],'r',linewidth=2)
#printMatrix(K[4:,4:])
plot(coords[:,0],coords[:,1],'o')
axis([-100,3500,-1600.,2000.])
print '--------Resolution'
du=solve(K[4:,4:],F[4:])

Du[2:,0]  = du[::2]
Du[2:,1]  = du[1::2]
Duf       = Du.flatten()
magnitude = 20.
print '--------Calcul des coordonnes deforme avec une magniture de:',magnitude
Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
sigmas=[]
print '--------Calcul des contraintes'
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls])
    sigmas.append(sigma)
masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
jet   = get_cmap('jet')
print '\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig
print '--------Visualisation de la deformee et des contraintes'

for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    print col
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)


show()
