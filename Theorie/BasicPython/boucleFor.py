#!/usr/bin/env python
# coding: utf-8

import numpy as np  

xs  = np.arange(0.,10,0.1)

print('Taille du vecteur xs:',xs.shape)

# Pour chaque element de xs, on va calculer  $$f(x)=1+2x^2$$
fxs = []                           # Préparation d une liste pour stocker les valeurs qui sont calculees dans la boucle
for x in xs:
    fx = 1.+2.*x**2                 # Calcul de la valeur de la fonction
    fxs.append(fx)                 # Le resultat est ajouté a la fin de la liste

print('Taille de fxs:',len(fxs))

print('Type de xs:',type(xs),' Type de fxs:', type(fxs)) # Le type informatique de chacune des objets informatiques

