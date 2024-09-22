#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt # importation du module pour tracer des graphiques
import numpy as np              # importation du module pour manipuler les tableaux (matrices)
x = np.arange(0.,6.*np.pi,0.1)  # Creation d un vecteur de valeurs allant de 0 à 6pi avec une distance de 0.1 entre chaque point

plt.plot(x,np.cos(x))              # Creation de la visualisation de la fonction cos(x)


plt.show()

plt.plot(x,np.cos(x))
plt.xlabel('Angle en radians')
plt.ylabel('cos(x)')

plt.show()                             # Dans un script, on demande de visualiser les graphes sinon il reste en mémoire

