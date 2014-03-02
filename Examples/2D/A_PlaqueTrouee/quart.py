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
import geompy
import math
import SALOMEDS

L     = 400.
l     = 150.
Rtrou = 25.

geompy.init_geom(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(Rtrou, 0, 0)
Sommet_2 = geompy.MakeVertex(l/2., 0, 0)
Sommet_3 = geompy.MakeVertex(l/2., L/2., 0)
Sommet_4 = geompy.MakeVertex(0, L/2., 0)
Sommet_5 = geompy.MakeVertex(0, Rtrou, 0)
Sommet_6 = geompy.MakeVertex(0, 0, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Arc_1 = geompy.MakeArcCenter(Sommet_6, Sommet_5, Sommet_1,False)
Plaque = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Arc_1], 1)
Haut = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Haut, [8])
Sym1 = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Sym1, [3])
Sym2 = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Sym2, [10])
Arc = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Arc, [12])

geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, Haut, 'Haut' )
geompy.addToStudyInFather( Plaque, Sym1, 'Sym1' )
geompy.addToStudyInFather( Plaque, Sym2, 'Sym2' )
geompy.addToStudyInFather( Plaque, Arc, 'Arc' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
