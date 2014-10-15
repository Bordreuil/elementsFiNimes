# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v7.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

Lplaque = 25.
eplaque = 4.

unsurracine2=1./2.

geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(eplaque, 0, 0)
Sommet_3 = geompy.MakeVertex(Lplaque, 0, 0)
Sommet_4 = geompy.MakeVertex(Lplaque, -eplaque/2., 0)
Sommet_5 = geompy.MakeVertex(eplaque, -eplaque/2., 0)
Sommet_6 = geompy.MakeVertex(0, -eplaque/2., 0)
Sommet_7 = geompy.MakeVertex(0, eplaque, 0)
Sommet_8 = geompy.MakeVertex(-Lplaque, eplaque, 0)
Sommet_9 = geompy.MakeVertex(-Lplaque, 0, 0)
Sommet_12 = geompy.MakeVertex(eplaque*unsurracine2, eplaque*unsurracine2, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_7)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_8)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_9)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_1)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_12)
Ligne_1_vertex_3 = geompy.GetSubShape(Ligne_1, [3])
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_12, Ligne_1_vertex_3)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_5_vertex_3 = geompy.GetSubShape(Ligne_5, [3])
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_2, Ligne_5_vertex_3)
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_6)
Ligne_10 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_5)
Ligne_8_vertex_2 = geompy.GetSubShape(Ligne_8, [2])
Ligne_11 = geompy.MakeLineTwoPnt(Sommet_5, Ligne_8_vertex_2)
Ligne_11_vertex_3 = geompy.GetSubShape(Ligne_11, [3])
Ligne_12 = geompy.MakeLineTwoPnt(Sommet_3, Ligne_11_vertex_3)
Ligne_11_vertex_2 = geompy.GetSubShape(Ligne_11, [2])
Ligne_13 = geompy.MakeLineTwoPnt(Ligne_11_vertex_2, Sommet_4)
Ligne_12_vertex_2 = geompy.GetSubShape(Ligne_12, [2])
Ligne_14 = geompy.MakeLineTwoPnt(Sommet_4, Ligne_12_vertex_2)
Face_1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
Face_2 = geompy.MakeFaceWires([Ligne_1, Ligne_5, Ligne_6], 1)
Face_3 = geompy.MakeFaceWires([Ligne_5, Ligne_7, Ligne_8], 1)
Face_4 = geompy.MakeFaceWires([Ligne_7, Ligne_9, Ligne_10, Ligne_11], 1)
Face_5 = geompy.MakeFaceWires([Ligne_11, Ligne_12, Ligne_13, Ligne_14], 1)
BoutA = geompy.MakeCompound([Face_1, Face_2, Face_3, Face_4, Face_5])
Gauche = geompy.CreateGroup(BoutA, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Gauche, [9])
Gorge = geompy.CreateGroup(BoutA, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Gorge, [16])
Sym = geompy.CreateGroup(BoutA, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Sym, [26, 35])
Effort = geompy.CreateGroup(BoutA, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Effort, [33])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Sommet_12, 'Sommet_12' )


geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudyInFather( Ligne_1, Ligne_1_vertex_3, 'Ligne_1:vertex_3' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudyInFather( Ligne_5, Ligne_5_vertex_3, 'Ligne_5:vertex_3' )
geompy.addToStudy( Ligne_8, 'Ligne_8' )
geompy.addToStudy( Ligne_9, 'Ligne_9' )
geompy.addToStudy( Ligne_10, 'Ligne_10' )
geompy.addToStudyInFather( Ligne_8, Ligne_8_vertex_2, 'Ligne_8:vertex_2' )
geompy.addToStudy( Ligne_11, 'Ligne_11' )
geompy.addToStudyInFather( Ligne_11, Ligne_11_vertex_3, 'Ligne_11:vertex_3' )
geompy.addToStudy( Ligne_12, 'Ligne_12' )
geompy.addToStudyInFather( Ligne_11, Ligne_11_vertex_2, 'Ligne_11:vertex_2' )
geompy.addToStudy( Ligne_13, 'Ligne_13' )
geompy.addToStudyInFather( Ligne_12, Ligne_12_vertex_2, 'Ligne_12:vertex_2' )
geompy.addToStudy( Ligne_14, 'Ligne_14' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudy( Face_4, 'Face_4' )
geompy.addToStudy( Face_5, 'Face_5' )
geompy.addToStudy( BoutA, 'BoutA' )
geompy.addToStudyInFather( BoutA, Gauche, 'Gauche' )
geompy.addToStudyInFather( BoutA, Gorge, 'Gorge' )
geompy.addToStudyInFather( BoutA, Sym, 'Sym' )
geompy.addToStudyInFather( BoutA, Effort, 'Effort' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
