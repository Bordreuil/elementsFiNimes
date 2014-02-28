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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/Polytech/ElementsFinis/2013/C_Treillis')

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
O_1 = geompy.MakeVertex(0, 0, 0)
OX_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
Distance = 2000.
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(2000, 0, 0)
Sommet_3 = geompy.MakeVertex(4000, 0, 0)
Sommet_4 = geompy.MakeVertex(6000, 0, 0)
Sommet_5 = geompy.MakeVertex(7000, 0, 0)
Sommet_6 = geompy.MakeVertex(8000, 0, 0)
Sommet_7 = geompy.MakeVertex(6000, 500, 0)
Sommet_8 = geompy.MakeVertex(4000, 1000, 0)
Sommet_9 = geompy.MakeVertex(2000, 500, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_6)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_7)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_8)
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_9)
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_1)
Ligne_10 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_9)
Ligne_11 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_3)
Ligne_12 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_4)
Assemblage_1 = geompy.MakeCompound([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Ligne_5, Ligne_6, Ligne_7, Ligne_8, Ligne_9, Ligne_10, Ligne_11, Ligne_12])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( O_1, 'O' )
geompy.addToStudy( OX_1, 'OX' )
geompy.addToStudy( OY_1, 'OY' )
geompy.addToStudy( OZ_1, 'OZ' )
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
geompy.addToStudy( Ligne_12, 'Ligne_12' )
geompy.addToStudy( Assemblage_1, 'Assemblage_1' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Maillage_1 = smesh.Mesh(Assemblage_1)
Regular_1D = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(1)
Nb_Segments_1.SetDistrType( 0 )
isDone = Maillage_1.Compute()
TOUT = Maillage_1.CreateEmptyGroup( SMESH.EDGE, 'TOUT' )
nbAdd = TOUT.AddFrom( Maillage_1.GetMesh() )
Group_1 = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Group_1' )
nbAdd = Group_1.Add( [ 6 ] )
Group_1.SetColor( SALOMEDS.Color( 1, 0.666667, 0 ))
Group_2 = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Group_2' )
nbAdd = Group_2.Add( [ 5 ] )
Group_2.SetColor( SALOMEDS.Color( 1, 0.666667, 0 ))
Group_2 = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Group_3' )
nbAdd = Group_2.Add( [ 1 ] )
Group_2.SetColor( SALOMEDS.Color( 1, 0.666667, 0 ))

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(TOUT, 'TOUT')
smesh.SetName(Group_1, 'Group_1')
smesh.SetName(Group_2, 'Group_2')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
