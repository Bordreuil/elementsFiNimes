#!/usr/bin/env python
# coding: utf-8
import numpy as np

ns = range(10)                       # Creation d une liste de 10 elements allant de 1 à 9

us = []                                # Initialisation de la liste stockant les resultats de la suite
for n in ns:
    u = n/(n+1)**2                     # Calcul de la suite
    us.append(u)

import matplotlib.pyplot as plt
plt.plot(ns,us)
plt.xlabel('Entier n')
plt.ylabel('Suite $u_n$')
# Ajout pour visualiser a l'écran le graphique
plt.show()
