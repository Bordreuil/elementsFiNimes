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


geompy.init_geom(theStudy)

from param import *

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(0, 6, 0)
Sommet_3 = geompy.MakeVertex(-LTole1,Tole1Ep, 0)
Sommet_4 = geompy.MakeVertex(-LTole1, 0, 0)
Sommet_5 = geompy.MakeVertex(LCordon, 0, 0)
Sommet_6 = geompy.MakeVertex(LCordon+DecTole2, Tole2Ep, 0)
Sommet_7 = geompy.MakeVertex(LCordon+DecTole2+AnalTole2,Tole2Ep,0)
Sommet_8 = geompy.MakeVertex(LTole2, Tole2Ep, 0)
Sommet_9 = geompy.MakeVertex(LTole2, 0, 0)

Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_1)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_5)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_6)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_7)
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_8)
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_9)
Ligne_10 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_5)
Ligne_11 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_2)
Tole1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
Cordon = geompy.MakeFaceWires([Ligne_1, Ligne_5, Ligne_6, Ligne_11], 1)
Tole2 = geompy.MakeFaceWires([Ligne_6, Ligne_7, Ligne_8, Ligne_9, Ligne_10], 1)
Joint = geompy.MakeCompound([Tole1, Cordon, Tole2])

GTole1 = geompy.CreateGroup(Joint, geompy.ShapeType["FACE"])
geompy.UnionIDs(GTole1, [2])

Cordon_1 = geompy.CreateGroup(Joint, geompy.ShapeType["FACE"])
geompy.UnionIDs(Cordon_1, [12])
GTole2 = geompy.CreateGroup(Joint, geompy.ShapeType["FACE"])
geompy.UnionIDs(GTole2, [19])
Encastre = geompy.CreateGroup(Joint, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Encastre, [9])
Anal = geompy.CreateGroup(Joint, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Effort, [25])
Anali = geompy.CreateGroup(Joint, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Anali, [23])
Effort = geompy.CreateGroup(Joint, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Effort, [29])

geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudy( Ligne_8, 'Ligne_8' )
geompy.addToStudy( Ligne_9, 'Ligne_9' )
geompy.addToStudy( Ligne_10, 'Ligne_10' )
geompy.addToStudy( Ligne_11, 'Ligne_11' )
geompy.addToStudy( Tole1, 'Tole1' )
geompy.addToStudy( Cordon, 'Cordon' )
geompy.addToStudy( Tole2, 'Tole2' )
geompy.addToStudy( Joint, 'Joint' )
geompy.addToStudyInFather( Joint, GTole1, 'Tole1' )
geompy.addToStudyInFather( Joint, Cordon_1, 'Cordon' )
geompy.addToStudyInFather( Joint, GTole2, 'Tole2' )
geompy.addToStudyInFather( Joint, Encastre, 'Encastre' )
geompy.addToStudyInFather( Joint, Effort, 'Effort' )
geompy.addToStudyInFather( Joint, Anal, 'Anal' )
geompy.addToStudyInFather( Joint, Anali, 'Anali' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
