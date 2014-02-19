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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/C_TuyauPoutre')

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
Encastre = geompy.MakeVertex(0, 0, 0)
DebutCoude = geompy.MakeVertex(0, 3000, 0)
FinCoude = geompy.MakeVertex(600, 3600, 0)
CentreCoude = geompy.MakeVertex(600, 3000, 0)
Effort = geompy.MakeVertex(3600, 3600, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Encastre, DebutCoude)
Ligne_2 = geompy.MakeLineTwoPnt(FinCoude, Effort)
Coude = geompy.MakeArcCenter(CentreCoude, DebutCoude, FinCoude,False)
Tuyau = geompy.MakeCompound([Ligne_1, Ligne_2, Coude])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Encastre, 'Encastre' )
geompy.addToStudy( DebutCoude, 'DebutCoude' )
geompy.addToStudy( FinCoude, 'FinCoude' )
geompy.addToStudy( CentreCoude, 'CentreCoude' )
geompy.addToStudy( Effort, 'Effort' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Coude, 'Coude' )
geompy.addToStudy( Tuyau, 'Tuyau' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Tuyau_1 = smesh.Mesh(Tuyau)
Regular_1D = Tuyau_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(15)
Nb_Segments_1.SetDistrType( 0 )
isDone     = Tuyau_1.Compute()
coincident_nodes_on_part = Tuyau_1.FindCoincidentNodesOnPart( Tuyau_1, 1e-05, [  ] )
Tuyau_1.MergeNodes([[ 2, 5 ], [ 3, 6 ]])
isDone     = Tuyau_1.Compute()
TOUT       = Tuyau_1.CreateEmptyGroup( SMESH.EDGE, 'TOUT' )
nbAdd      = TOUT.AddFrom( Tuyau_1.GetMesh() )
Encastre_1 = Tuyau_1.CreateEmptyGroup( SMESH.NODE, 'Encastre' )
nbAdd      = Encastre_1.Add( [ 1 ] )
Effort_1   = Tuyau_1.CreateEmptyGroup( SMESH.NODE, 'Effort' )
nbAdd      = Effort_1.Add( [ 4 ] )
isDone     = Tuyau_1.Compute()


## set object names
smesh.SetName(Tuyau_1.GetMesh(), 'Tuyau')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(TOUT, 'TOUT')
smesh.SetName(Encastre_1, 'Encastre')
smesh.SetName(Effort_1, 'Effort')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
