# -*- coding: utf-8 -*-
# Fichier : visuCordon.py
# Fait partie de l'exemple sur le calcul des contraintes
# dans un assemblage modéliser en plaque.

from pylab import *

datas=loadtxt('cordon.dat')

X     = datas[:,:2]
ind   = X[:,0].argsort()
X     = X[ind,:]

NYY   = datas[ind,2]
NXX   = datas[ind,3]

plot(X[:,0],NYY,X[:,0],NXX)
show()
