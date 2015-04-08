# -*- coding: utf-8 -*-
# Fichier : visuContrainte.py
# Fait partie de l'exemple sur le calcul des contraintes
# dans le fond de gorge: 2D/C_BoutABout


from pylab import *

# On charge le fichier de resultat qui doit avoir
# la structure suivante :
# COOR_X,COOR_Y,SIXX,SIYY,XIXY 
datas = loadtxt('contraintes.txt')
# On récupère les coordonnées
X     = datas[:,:2]
# On calcul l'orientation du plan de gorge
print 'orientation fonde gorge:',arctan2(X[-1,1],X[-1,0])
th    = arctan2(X[0,1],X[0,0])-pi/2.
# On cherche les indices pour avoir X croissant
ind   = X[:,0].argsort()
# On reorganise le tableau de coordonnees...
X     = X[ind,:]
#....et de contraintes
SIXX  = datas[ind,2]
SIYY  = datas[ind,3]
SIXY  = datas[ind,4]
# On calcul le tenseur des contraintes en chacun des points
sigma = [] 
for i in range(SIXX.shape[0]):
    sigma.append(array([[SIXX[i],SIXY[i]],
                        [SIXY[i],SIYY[i]]],'d'))

# On les calcul dans le plan de gorge.
sigma    = array(sigma,'d')             # Contrainte pour tous les points
normal   = array([cos(th),sin(th)],'d') # normal a la facette
tangente =  array([cos(th+pi/2.),
                   sin(th+pi/2.)],'d')# tangente a la facette
vCont    = dot(sigma,normal)            # vecteur contrainre

snormal  = dot(vCont,normal)            # contrainte normale a la facette
stangent = dot(vCont,tangente)          # contrainte tangentiel a la facette

sigeq    = sqrt(snormal**2.+3.*stangent**2.)
# On trace les contraintes normale, tangentielle et équivalente
# en chaque point du fond de gorge
plot(X[:,0],snormal,'^-',
     X[:,0],stangent,'o-',
     X[:,0],sigeq,
     linewidth=2,markersize=8)


hold('on')

# On calcul pour la formule du code de construction
# qui suppose la contrainte constante le long du fond de gorge.

epaiss      = 4.
a           = epaiss/sqrt(2.)
effortparmm = 5*epaiss/2.
sn          = effortparmm/a*cos(th+pi/2.)**2.
tau         = effortparmm/a*sin(th+pi/2)*cos(th+pi/2.)

seq = sqrt(sn**2.+3.*tau**2.)

plot(X[:,0],ones(X.shape[0])*seq,'.-',linewidth=2.) 

legend(['Contrainte normale',
        'Contrainte tangentielle',
        'Contrainte equivalente',
        'Contrainte code'])
xlabel('Absice en mm le long du plan de gorge')
ylabel('Contrainte en MPa')
show()
