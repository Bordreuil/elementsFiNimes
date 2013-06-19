# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook


import iparameters
ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", 1), True)


ipar.append("AP_MODULES_LIST", "Geometry")
ipar.append("AP_MODULES_LIST", "Mesh")


###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS


geompy.init_geom(theStudy)

Centre = geompy.MakeVertex(0, 0, 0)
Vertex_droite = geompy.MakeVertex(6, 34, 0)
Vertex_gauche = geompy.MakeVertex(-6, 34, 0)
Arc_1 = geompy.MakeArcCenter(Centre, Vertex_droite, Vertex_gauche,False)
[geomObj_1] = geompy.SubShapeAll(Arc_1, geompy.ShapeType["EDGE"])
[geomObj_2] = geompy.SubShapeAll(Arc_1, geompy.ShapeType["EDGE"])
centre_loin = geompy.MakeVertex(0, 0, 42)
Line_extrusion = geompy.MakeLineTwoPnt(centre_loin, Centre)

Plaque = geompy.MakePrismVecH(Arc_1, Line_extrusion, -42)
listSubShapeIDs = geompy.SubShapeAllIDs(Plaque, geompy.ShapeType["EDGE"])
[Edge_1,Edge_2,Edge_3,Edge_4] = geompy.ExtractShapes(Plaque, geompy.ShapeType["EDGE"], True)
listSubShapeIDs = geompy.SubShapeAllIDs(Plaque, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Plaque, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_1)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_2)


listSubShapeIDs = geompy.SubShapeAllIDs(Plaque, geompy.ShapeType["EDGE"])

[geomObj_3,geomObj_4] = geompy.SubShapeAll(Edge_2, geompy.ShapeType["VERTEX"])
[geomObj_5] = geompy.SubShapeAll(Edge_2, geompy.ShapeType["EDGE"])
[geomObj_6] = geompy.SubShapeAll(Edge_2, geompy.ShapeType["EDGE"])

[geomObj_7] = geompy.SubShapeAll(Edge_3, geompy.ShapeType["EDGE"])
[geomObj_8] = geompy.SubShapeAll(Edge_3, geompy.ShapeType["EDGE"])

[geomObj_9] = geompy.SubShapeAll(Edge_4, geompy.ShapeType["EDGE"])
[geomObj_10] = geompy.SubShapeAll(Edge_4, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_3)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_4)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_5)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_6)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_9)
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_10)
Encastre = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Encastre, [9])
geomObj_11 = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(geomObj_11, [3])
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_7)
Moment = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Moment, [10])
listSameIDs = geompy.GetSameIDs(Plaque, geomObj_8)
geompy.addToStudy( Centre, 'Centre' )
geompy.addToStudy( Vertex_droite, 'Vertex_droite' )
geompy.addToStudy( Vertex_gauche, 'Vertex_gauche' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( centre_loin, 'centre_loin' )
geompy.addToStudy( Line_extrusion, 'Line_extrusion' )
geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, Edge_2, 'Edge_2' )
geompy.addToStudyInFather( Plaque, Edge_3, 'Edge_3' )
geompy.addToStudyInFather( Plaque, Edge_4, 'Edge_4' )
geompy.addToStudyInFather( Plaque, Encastre, 'Encastre' )
geompy.addToStudyInFather( Plaque, Moment, 'Moment' )

### Store presentation parameters of displayed objects
import iparameters
ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "GEOM", 1))

#Set up entries:

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import NETGENPlugin
Mesh_1 = smesh.Mesh(Plaque)
NETGEN_2D = Mesh_1.Triangle(algo=smesh.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetMaxSize( 1 )
NETGEN_2D_Parameters.SetMinSize( 0.5 )
isDone = Mesh_1.Compute()
Encastre_1 = Mesh_1.GroupOnGeom(Encastre,'Encastre',SMESH.EDGE)
Moment_1 = Mesh_1.GroupOnGeom(Moment,'Moment',SMESH.EDGE)
Plaque_1 = Mesh_1.GroupOnGeom(Plaque,'Plaque',SMESH.FACE)

## set object names
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Parameters, 'NETGEN 2D Parameters')
smesh.SetName(Encastre_1, 'Encastre')
smesh.SetName(Moment_1, 'Moment')
smesh.SetName(Plaque_1, 'Plaque')

### Store presentation parameters of displayed objects
import iparameters
ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "SMESH", 1))



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
  iparameters.getSession().restoreVisualState(1)
