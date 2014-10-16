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


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
O_1 = geompy.MakeVertex(0, 0, 0)
OX_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
O_2 = geompy.MakeVertex(0, 0, 0)
OX_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_2 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_2 = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(500, 0, 0)
Sommet_3 = geompy.MakeVertex(500, 500, 0)
Sommet_4 = geompy.MakeVertex(0, 500, 0)
Sommet_5 = geompy.MakeVertex(250, 100, 0)
Sommet_6 = geompy.MakeVertex(250, 400, 0)
Sommet_8 = geompy.MakeVertex(250, 400, 500)
Sommet_9 = geompy.MakeVertex(250, 100, 500)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
[geomObj_1] = geompy.SubShapeAll(Ligne_2, geompy.ShapeType["EDGE"])
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_1)
[geomObj_2] = geompy.SubShapeAll(Ligne_4, geompy.ShapeType["EDGE"])
[geomObj_3] = geompy.SubShapeAll(Ligne_4, geompy.ShapeType["EDGE"])
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_6)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_8)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_9)
Ligne_5_vertex_2 = geompy.GetSubShape(Ligne_5, [2])
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_9, Ligne_5_vertex_2)
Face_1 = geompy.MakeFaceWires([Ligne_5, Ligne_6, Ligne_7, Ligne_8], 1)
Face_2 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
Partition_1 = geompy.MakePartition([Face_2], [Face_1], [], [], geompy.ShapeType["FACE"], 0, [], 0)
[geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9] = geompy.SubShapeAll(Partition_1, geompy.ShapeType["VERTEX"])
[Ar_te_1] = geompy.SubShapes(Partition_1, [12])
Te = geompy.MakeCompound([Face_1, Partition_1])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["SHAPE"])
listSameIDs = geompy.GetSameIDs(Te, geomObj_1)
listSameIDs = geompy.GetSameIDs(Te, geomObj_2)
listSameIDs = geompy.GetSameIDs(Te, geomObj_3)
listSameIDs = geompy.GetSameIDs(Te, geomObj_4)
listSameIDs = geompy.GetSameIDs(Te, geomObj_5)
listSameIDs = geompy.GetSameIDs(Te, geomObj_6)
listSameIDs = geompy.GetSameIDs(Te, geomObj_7)
listSameIDs = geompy.GetSameIDs(Te, geomObj_8)
listSameIDs = geompy.GetSameIDs(Te, geomObj_9)
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["SHAPE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["SHAPE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["SHAPE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Te, geompy.ShapeType["SHAPE"])

geomObj_10 = geompy.CreateGroup(Te, geompy.ShapeType["EDGE"])
geompy.UnionIDs(geomObj_10, [23, 17])
Effort = geompy.CreateGroup(Te, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Effort, [9])
geomObj_11 = geompy.CreateGroup(Te, geompy.ShapeType["EDGE"])
geompy.UnionIDs(geomObj_11, [4])
FaceSup = geompy.CreateGroup(Te, geompy.ShapeType["FACE"])
geompy.UnionIDs(FaceSup, [2])

[geomObj_12] = geompy.GetSharedShapes(Te, geomObj_5, geompy.ShapeType["VERTEX"])
[geomObj_13] = geompy.GetSharedShapes(Te, geomObj_9, geompy.ShapeType["VERTEX"])
geomObj_14 = geompy.CreateGroup(FaceSup, geompy.ShapeType["EDGE"])
geompy.UnionIDs(geomObj_14, [3])

Encastre = geompy.CreateGroup(Te, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Encastre, [17, 19])
Cordon = geompy.CreateGroup(Te, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Cordon, [23])



geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( O_1, 'O' )

geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudyInFather( Ligne_5, Ligne_5_vertex_2, 'Ligne_5:vertex_2' )
geompy.addToStudy( Ligne_8, 'Ligne_8' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( Te, 'Te' )

geompy.addToStudyInFather( Te, Effort, 'Effort' )
geompy.addToStudyInFather( Te, FaceSup, 'FaceSup' )

geompy.addToStudyInFather( Te, Encastre, 'Encastre' )
geompy.addToStudyInFather( Te, Cordon, 'Cordon' )
geompy.addToStudyInFather( Partition_1, Ar_te_1, 'Arête_1' )


###
### ASTER component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
