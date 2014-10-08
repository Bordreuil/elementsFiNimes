# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

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

L     = 400.
l     = 150.
Rtrou = 25.
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(l, 0, 0)
Sommet_3 = geompy.MakeVertex(l, L, 0)
Sommet_4 = geompy.MakeVertex(0, L, 0)
Sommet_5 = geompy.MakeVertex(l/2.,L/2., 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_1)
Cercle_1 = geompy.MakeCircle(Sommet_5, None, Rtrou)
Plaque = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Cercle_1], 1)
Bas = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Bas, [3])
Haut = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Haut, [8])
Trou = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Trou, [12])



geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Cercle_1, 'Cercle_1' )

geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, Bas, 'Bas' )
geompy.addToStudyInFather( Plaque, Haut, 'Haut' )
geompy.addToStudyInFather( Plaque, Trou, 'Trou' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
