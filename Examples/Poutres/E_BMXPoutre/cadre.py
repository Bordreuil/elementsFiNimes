# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()

import salome_notebook
notebook = salome_notebook.notebook


###
### GEOM component
###

import GEOM
import math
import SALOMEDS
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)


x_0 = 0.;   y_0 = 0.;
x_1 = 5.;   y_1 = -100.;
x_2 = -500.;y_2 = -10.;
x_3 = -475.;y_3 = -400.;
x_4 = -550.;y_4 = -425.; z_4 = 50.;
x_5 = -530.;y_5 = -50.;  z_5 = 40.;
x_6 = -900.;y_6 = -480.; z_6 = 85.;
x_7 = 75. ;y_7 = -450 ;z_7=0.;

# Definition des points
Sommet_1   = geompy.MakeVertex(x_0 ,y_0 , 0.)
Sommet_2   = geompy.MakeVertex(x_1 ,y_1 , 0.)
Sommet_3   = geompy.MakeVertex(x_2 ,y_2 , 0.)
Sommet_4   = geompy.MakeVertex(x_3 ,y_3 , 0.)
Sommet_5   = geompy.MakeVertex(x_4 ,y_4 , z_4)
Sommet_6   = geompy.MakeVertex(x_4 ,y_4 , -z_4)
Sommet_7   = geompy.MakeVertex(x_5 ,y_5 , z_5)
Sommet_8   = geompy.MakeVertex(x_5 ,y_5 , -z_5)
Sommet_9   = geompy.MakeVertex(x_6 ,y_6 , z_6)
Sommet_10  = geompy.MakeVertex(x_6 ,y_6 ,-z_6)
Sommet_11  = geompy.MakeVertex(x_7 ,y_7 , z_7)


Direction = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Barre_sup = geompy.MakeLineTwoPnt(Sommet_1, Sommet_3)
Barre_inf = geompy.MakeLineTwoPnt(Sommet_2, Sommet_4)
Barre_selle = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Arriere_bas_1 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Arriere_bas_2 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_6)
Arriere_bas_3 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_10)
Arriere_bas_4 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_9)
Arriere_haut_1 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_7)
Arriere_haut_2 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_8)
Arriere_haut_3 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_10)
Arriere_haut_4 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_9)
Fourche = geompy.MakeLineTwoPnt(Sommet_2, Sommet_11)
Cadre = geompy.MakeCompound([Direction, Barre_sup, Barre_inf, Barre_selle, Fourche, Arriere_bas_1, Arriere_bas_2, Arriere_bas_3, Arriere_bas_4, Arriere_haut_1, Arriere_haut_2, Arriere_haut_3, Arriere_haut_4])
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Sommet_10, 'Sommet_10' )
geompy.addToStudy( Sommet_11, 'Sommet_11' )
geompy.addToStudy( Direction, 'Direction' )
geompy.addToStudy( Barre_sup, 'Barre_sup' )
geompy.addToStudy( Barre_inf, 'Barre_inf' )
geompy.addToStudy( Barre_selle, 'Barre_selle' )
geompy.addToStudy( Arriere_bas_1, 'Arriere_bas_1' )
geompy.addToStudy( Arriere_bas_2, 'Arriere_bas_2' )
geompy.addToStudy( Arriere_bas_3, 'Arriere_bas_3' )
geompy.addToStudy( Arriere_bas_4, 'Arriere_bas_4' )
geompy.addToStudy( Arriere_haut_1, 'Arriere_haut_1' )
geompy.addToStudy( Arriere_haut_2, 'Arriere_haut_2' )
geompy.addToStudy( Arriere_haut_3, 'Arriere_haut_3' )
geompy.addToStudy( Arriere_haut_4, 'Arriere_haut_4' )
geompy.addToStudy( Fourche, 'Fourche' )
geompy.addToStudy( Cadre, 'Cadre' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
