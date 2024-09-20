import sys
sys.path.append('..')


from barreElement2d import *
from matrixTools    import *
from visuTools import *
import matplotlib.pyplot  as plt
from numpy import *
from numpy.linalg import *

#Resolution d un probleme de structure treillis
#Cette méthode est la plus générale possible, on peut tout résoudre avec, il suffit de bien rentrer toutes les données 


L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2

#definition du maillage qui change en fonction du problème
#prendre les racines pour des problèmes avec des barres inclinéess
"-------------------------------------------------------------------------------------------------"
coords =array([[0.,0.],                       
               [0.,L_barre],
               [L_barre,0.],
               [L_barre,L_barre],    
               [2.*L_barre,0.],      
               [2.*L_barre,L_barre],
               [3.*L_barre,0.],
               [3.*L_barre,L_barre]]   ,'d') 
               
"-------------------------------------------------------------------------------------------------"
#situer les points et les coordonées fait par jules 
('Montrer les coordonées des points pour michel le trizomique')
plt.figure()
plt.plot(coords[:,0],coords[:,1],'o')
taille=np.shape(coords)
title('coordonées des points pour situer les neuds')


for i in range(taille[0]):
    plt.annotate('%s'%i, xy=(coords[i,0],coords[i,1]))
plt.show()
plt.figure()




imposedDofs   = [11,12,13,14,15]  # Points bloqués 
#pairs x 
#impairs y 



valuesImposed = [0,0,0,0,0] 
# impose la valeur qu'on veut 0 = pas des dep
#ici 5 el 



# 8 neuds x 2 ddl = 16 ddlssidiff0 pb 
ddlsActive   = listActiveDofs(16, imposedDofs) 
#ddlsactive  = liste degres(16)-degres imposés(4)



print('Taille de coords:',coords.shape)
Du  = zeros((8,2),'d') 
# 8 est le nb de noeuds et 2 est le nb d'inconnues sur chaque noeud







# la je decouperais les eléments du code donné 
"------------------------------------------------------------------------------------------------"
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

ndofs = 16 # Car on a 16 noeuds du au 8*2=16
K         = zeros((ndofs,ndofs),'d')

F         = zeros((ndofs,),'d') 

"----------------------------------------------------------------------"
# attention de ne pas imoser des dofs qui n existent pas ! 
#



F[1] =-6500. # forces pair sur x impair sur y attention aux signes +/- 

# forces pair sur x impair sur y attention aux signes +/-




print('Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    K = assembMatrix(K, k, ddls)

Kglob=K.copy() #on copie K comme cela on pourras comparer K et Kglob 
KglobnonModif = K.copy()
for i,dof in enumerate(imposedDofs):
    Kglob[dof,:] = 0;Kglob[dof,dof] = 1;F[dof] = valuesImposed[i]

# show()
# ON BLOQUE LES PTS 0 ET 6 
# on doit mettre Uo, Vo, U6 et V6 ===0
# En 2 tps : on va commencer par la définitions des degrés de libérté qui sont bloqués
# Et après on découpe la matrice globale 

print('Resolution') 
du      = solve(Kglob,F) 
du      = linalg.solve(Kglob,F) 
Du[:,0] = du[::2] # compte de 2 en 2 à partir de 0 pour les x 
Y       = dot(KglobnonModif[1,:],du)
Du[:,1] = du[1::2] # compte de 2 en 2 pour les y

# on résoud toutes les lignes du coup pas besoins de séléctionner les lignes qu'on cherche à résoudre







magnitude = 50.
#Magnetude 100 on voit bien les deplacementrs 
#mais on sort du cadre 







print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
print(Du)
Duf = Du.flatten()  

# Duf c'est la matrice de déplacement de tous les pts qui est sur une seule colonne U0,V0,U1,V1,U2..

Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
figure()
title('Contraintes')
sigmas=[]
print('--------Calcul des contraintes')
for el in els:
    ddls  = el.ddls()
    sigma = el.calculContrainte(Duf[ddls]) # On calcule les contraintes avec fct qui est dans le fichier 
    sigmas.append(sigma)                   # On calcule en projetant les deux ddl dans le repère de l'élement
print(sigmas)
plotNodes(Coords)
masig   = max(sigmas)
misig   = min(sigmas)
DeltaS  = masig-misig
jet     = get_cmap('jet')
plotContraintes(els,Coords,sigmas,jet)
axis([-100,3.*L_barre+100,-100.,L_barre+100.])
show()
figure()
title('deplacements')
print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)
print('Visualisation de la deformee et des contraintes')

for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)

axis([-100,3.*L_barre+100,-100.,L_barre+100.])


show()

# exercices 
# https://github.com/Bordreuil/elementsFiNimes/tree/master/Theorie/Barre2d?fbclid=IwAR0OYDdZMKoZGETWok6IwRWt3I5IGOT9NYstoPfTP8WvAFynMSDk8keVq3c
