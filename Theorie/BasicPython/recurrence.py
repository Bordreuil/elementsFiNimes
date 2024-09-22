#!/usr/bin/env python
# coding: utf-8

# On veut calculer une suite definie par recurrence avec $u_0=5$ et $u_{n+1}=2*u_n+(n+2)^2$.
# 
# On a besoin d'une liste d'entier, d'un stockage du resultat.

import numpy as np

uns = [5]                  # Creation de la liste pour stocker les termes de la suite par recurrence

for n in range(1,10):
    unp1 = 2*uns[-1]+(n+2)**2
    uns.append(unp1)
    print(uns)

