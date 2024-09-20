# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:38:45 2022

@author: jules.robin
"""
import sys
sys.path.append('..')
from barreElement2d import *
from matrixTools    import *
from visuTools import *
import matplotlib.pyplot  as plt
from numpy import *
from numpy.linalg import *

#  Resolution d un probleme de structure treillis
# Cette méthode est la plus générale possible, on peut tout résoudre avec, il suffit de bien rentrer toutes les données 


L_barre = 1000.     # mm
E       = 200000.  # MPa
S       = 200.     # mm**2


coords =array([[0.,0.],                       
               [2.*L_barre,0.],
               [3.*L_barre,0.],
               [2.*L_barre,L_barre],    
               [0.,2.*L_barre],      
               [2.*L_barre,2.*L_barre],
               [3.*L_barre,2.*L_barre],
               [5.*L_barre,L_barre]]   ,'d') 

imposedDofs   = [0,1,3,8,9]  # Définitions des pts qui sont bloqués 
valuesImposed = [0,0,0,0,0] # Cette méthode permet d'imposer la valeur qu'on veut
# 8 neuds x 2 ddl = 16 ddls
ddlsActive = listActiveDofs(coords.shape[0]*2 , imposedDofs) # listActiveDofs permet de renvoyer les degrès actif en fonction de tous les degrès qu'on a et ceux qui sont imposés 


Du  = zeros((8,2),'d') # 8 est le nb de noeuds et 2 est le nb d'inconnues sur chaque noeuds

###############################################################################
el1 = barre2D([0,1],2.*L_barre,E,S,0.*pi/180.)
el2 = barre2D([1,2],L_barre,E,S,0.*pi/180.)
el3 = barre2D([0,5],sqrt(2.)*2.*L_barre,E,S,45.*pi/180.)
el4 = barre2D([0,4],L_barre,E,S,90.*pi/180.)
el5 = barre2D([4,5],2.*L_barre,E,S,0.*pi/180.)
el6 = barre2D([5,6],L_barre,E,S,0.*pi/180.)
el7 = barre2D([1,3],L_barre,E,S,90.*pi/180.)
el8 = barre2D([3,5],L_barre,E,S,90.*pi/180.)
el9 = barre2D([2,3],sqrt(2.)*L_barre,E,S,135.*pi/180.)
el10 = barre2D([3,6],sqrt(2.)*L_barre,E,S,45.*pi/180.)
el11 = barre2D([2,6],2.*L_barre,E,S,90.*pi/180.)
el12 = barre2D([6,7],sqrt(5.)*L_barre,E,S,-63.*pi/180.)
el13 = barre2D([2,7],sqrt(5.)*L_barre,E,S,63.*pi/180.)


els=[el1,el2,el3,el4,el5,el6,el7,el8,el9,el10,el11,el12,el13]

###############################################################################

ndofs = coords.shape[0]*2 
K = zeros((ndofs,ndofs),'d')
F         = zeros((ndofs,),'d') 

F[14] =7071. 
F[15] =7071. 


print('--------Assemblage des matrices de rigidite elementaires')
for el in els:
    k    = el.stiffness()
    ddls = el.ddls()
    K = assembMatrix(K, k, ddls)
    # conn = el.connectivite()                              #Ancienne méthode
    # Kglob=assembMatrix(Kglob,k,ddls)                      #C'était pour faire les barres
    # plot(coords[conn,0],coords[conn,1],'r',linewidth=2)   #On a remplacé Kglob par K puis on copie K sur Kglob

Kglob=K.copy()
KglobnonModif = K.copy()
for i,dof in enumerate(imposedDofs):
    Kglob[dof,:] = 0;Kglob[dof,dof] = 1;F[dof] = valuesImposed[i]

# show()
################################################
# ON BLOQUE LES PTS 0 ET 6 
# on doit mettre Uo, Vo, U6 et V6 ===0
# En 2 tps : on va commencer par la définitions des degrés de libérté qui sont bloqués
# Et après on découpe la matrice globale 
################################################
print('--------Resolution') 
du = solve(Kglob,F) 
du = linalg.solve(Kglob,F) 
Du[:,0] = du[::2] # compte de 2 en 2 à partir de 0
Y = dot(KglobnonModif[1,:],du)
Du[:,1] = du[1::2] # compte de 2 en 2 à partir de 1

# on résoud toutes les lignes du coup pas besoins de séléctionner les lignes qu'on cherche à résoudre

magnitude = 100.
print('--------Calcul des coordonnes deforme avec une magniture de:',magnitude)
print(Du)
Duf = Du.flatten()  # Duf c'est la matrice de déplacement de tous les pts qui est sur une seule colonne U0,V0,U1,V1,U2..

Coords     = coords+magnitude*Du
plot(Coords[:,0],Coords[:,1],'o')
show()
figure()
title('Contraintes')
sigmas=[]
print('--------Calcul des contraintes')
for el in els:
    ddls = el.ddls()
    sigma = el.calculContrainte(Duf[ddls]) # On calcul les contraintes avec fct qui est dans le fichier 
    sigmas.append(sigma)                    # On calcul en projetant les deux ddl dans le repère de l'élement
print(sigmas)
##########################################################################
# CALCUL DE LA FORCE
force = np.zeros((12,))
for i in imposedDofs:
    force[i] =sigmas[i] * S
print(force)
##########################################################################
plotNodes(Coords)
masig = max(sigmas)
misig = min(sigmas)
DeltaS = masig-misig
jet   = get_cmap('jet')
plotContraintes(els,Coords,sigmas,jet)
axis([-100,5500,-1600.,3000.])
show()
figure()
title('depl')
print('\tContrainte Maxi:\t',masig,' Contrainte Min:\t',misig)
print('--------Visualisation de la deformee et des contraintes')

for i,el in enumerate(els):
    conn = el.connectivite()
    col  = (sigmas[i]-misig)/DeltaS
    plot(Coords[conn,0],Coords[conn,1],color=jet(col),linewidth=3)

axis([-100,5500,-1600.,3000.])


show()
