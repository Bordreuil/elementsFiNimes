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
Sommet_2 = geompy.MakeVertex(0, 1, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Maillage_1 = smesh.Mesh(Ligne_1)
Regular_1D = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(20)
Nb_Segments_1.SetDistrType( 0 )
isDone = Maillage_1.Compute()
POUTRE = Maillage_1.GroupOnGeom(Ligne_1,'Ligne_1',SMESH.EDGE)
POUTRE_1 = Maillage_1.GroupOnGeom(Ligne_1,'Ligne_1',SMESH.NODE)
POUTRE_1.SetName( 'POU§TRE' )
POUTRE_1.SetName( 'POUTRE' )
POUTRE.SetName( 'POUTRE' )
Encastre = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Encastre' )
nbAdd = Encastre.Add( [ 1 ] )
Effort = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Effort' )
nbAdd = Effort.Add( [ 2 ] )
isDone = Maillage_1.Compute()
[ POUTRE, POUTRE_1, Encastre, Effort ] = Maillage_1.GetGroups()
smesh.SetName(Maillage_1, 'Maillage_1')

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(POUTRE, 'POUTRE')
smesh.SetName(POUTRE_1, 'POUTRE')
smesh.SetName(Encastre, 'Encastre')
smesh.SetName(Effort, 'Effort')
###



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
