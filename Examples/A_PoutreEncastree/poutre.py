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
#sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/A_PoutreEncastree')





###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS


geompy.init_geom(theStudy)

Sommet_1 = geompy.MakeVertex(0, 0, 0)
[geomObj_1] = geompy.SubShapeAll(Sommet_1, geompy.ShapeType["VERTEX"])
[geomObj_2] = geompy.SubShapeAll(Sommet_1, geompy.ShapeType["VERTEX"])

Sommet_2 = geompy.MakeVertex(1000, 0, 0)
[geomObj_3] = geompy.SubShapeAll(Sommet_2, geompy.ShapeType["VERTEX"])
[geomObj_4] = geompy.SubShapeAll(Sommet_2, geompy.ShapeType["VERTEX"])

Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)

listSubShapeIDs = geompy.SubShapeAllIDs(Ligne_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Ligne_1, geompy.ShapeType["VERTEX"])
listSameIDs = geompy.GetSameIDs(Ligne_1, geomObj_1)
Encastre = geompy.CreateGroup(Ligne_1, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Encastre, [2])

listSameIDs = geompy.GetSameIDs(Ligne_1, geomObj_2)
listSameIDs = geompy.GetSameIDs(Ligne_1, geomObj_3)
Effort = geompy.CreateGroup(Ligne_1, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Effort, [3])

listSameIDs = geompy.GetSameIDs(Ligne_1, geomObj_4)
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudyInFather( Ligne_1, Encastre, 'Encastre' )
geompy.addToStudyInFather( Ligne_1, Effort, 'Effort' )

### Store presentation parameters of displayed objects
import iparameters
ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "GEOM", 1))

#Set up entries:
# set up entry GEOM_1 (Sommet_1) parameters
objId = geompy.getObjectID(Sommet_1)

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Maillage_1    = smesh.Mesh(Ligne_1)
Regular_1D    = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(10)
Nb_Segments_1.SetDistrType( 0 )
isDone        = Maillage_1.Compute()
Encastre_1    = Maillage_1.GroupOnGeom(Encastre,'Encastre',SMESH.NODE)
Effort_1      = Maillage_1.GroupOnGeom(Effort,'Effort',SMESH.NODE)
TOUT          = Maillage_1.GroupOnGeom(Ligne_1,'Ligne_1',SMESH.EDGE)
TOUT.SetName( 'TOUT' )

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Encastre_1, 'Encastre')
smesh.SetName(Effort_1, 'Effort')
smesh.SetName(TOUT, 'TOUT')




if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
  iparameters.getSession().restoreVisualState(1)
