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

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(1, 0, 0)
Sommet_3 = geompy.MakeVertex(1, 1, 0)
Sommet_4 = geompy.MakeVertex(0, 1, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_1)
Plaque = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
listSubShapeIDs = geompy.SubShapeAllIDs(Plaque, geompy.ShapeType["EDGE"])
BORD = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(BORD, [3, 6, 8, 10])
geomObj_1 = geompy.GetSubShape(Plaque, [3])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, BORD, 'BORD' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import NETGENPlugin
Maillage_1 = smesh.Mesh(Plaque)
NETGEN_2D = Maillage_1.Triangle(algo=smesh.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetMaxSize( 0.1 )
NETGEN_2D_Parameters.SetSecondOrder( 0 )
NETGEN_2D_Parameters.SetOptimize( 1 )
NETGEN_2D_Parameters.SetFineness( 2 )
NETGEN_2D_Parameters.SetMinSize( 0.002 )
NETGEN_2D_Parameters.SetQuadAllowed( 0 )
isDone = Maillage_1.Compute()
BORD_1 = Maillage_1.GroupOnGeom(BORD,'BORD',SMESH.EDGE)
BORD_2 = Maillage_1.GroupOnGeom(BORD,'BORD',SMESH.NODE)
Plaque_1 = Maillage_1.GroupOnGeom(Plaque,'Plaque',SMESH.FACE)
[ BORD_1, BORD_2, Plaque_1 ] = Maillage_1.GetGroups()
smesh.SetName(Maillage_1, 'Maillage_1')
Maillage_1.ExportMED( r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Plaques/E_Modes/mode.mmed', 0, SMESH.MED_V2_2, 1 )

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Parameters, 'NETGEN 2D Parameters')
smesh.SetName(BORD_1, 'BORD')
smesh.SetName(BORD_2, 'BORD')
smesh.SetName(Plaque_1, 'Plaque')



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
