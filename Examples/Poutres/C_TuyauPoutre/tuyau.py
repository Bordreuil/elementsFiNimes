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
# sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Poutres/C_TuyauPoutre')

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
geompy.addToStudy( O_1, 'O' )
geompy.addToStudy( OX_1, 'OX' )
geompy.addToStudy( OY_1, 'OY' )
geompy.addToStudy( OZ_1, 'OZ' )
geompy.addToStudy( Encastre, 'Encastre' )
geompy.addToStudy( DebutCoude, 'DebutCoude' )
geompy.addToStudy( FinCoude, 'FinCoude' )
geompy.addToStudy( CentreCoude, 'CentreCoude' )
geompy.addToStudy( Effort, 'Effort' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Coude, 'Coude' )
geompy.addToStudy( Tuyau, 'Tuyau' )

# ###
# ### SMESH component
# ###

# import  SMESH, SALOMEDS
# from salome.smesh import smeshBuilder

# smesh = smeshBuilder.New(theStudy)
# Tuyau_1 = smesh.Mesh(Tuyau)
# Regular_1D = Tuyau_1.Segment()
# Nb_Segments_1 = Regular_1D.NumberOfSegments(15,[],[])
# Nb_Segments_1.SetDistrType( 0 )
# coincident_nodes_on_part = Tuyau_1.FindCoincidentNodesOnPart( Tuyau_1, 1e-05, [] )
# Tuyau_1.MergeNodes([[ 2, 5 ], [ 3, 6 ]])
# TOUT = Tuyau_1.CreateEmptyGroup( SMESH.EDGE, 'TOUT' )
# nbAdd = TOUT.AddFrom( Tuyau_1.GetMesh() )
# Encastre_1 = Tuyau_1.CreateEmptyGroup( SMESH.NODE, 'Encastre' )
# nbAdd = Encastre_1.Add( [ 1 ] )
# Effort_1 = Tuyau_1.CreateEmptyGroup( SMESH.NODE, 'Effort' )
# nbAdd = Effort_1.Add( [ 4 ] )
# isDone = Tuyau_1.Compute()


# ## Set names of Mesh objects
# smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
# smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
# smesh.SetName(Tuyau_1.GetMesh(), 'Tuyau')
# smesh.SetName(TOUT, 'TOUT')
# smesh.SetName(Effort_1, 'Effort')
# smesh.SetName(Encastre_1, 'Encastre')

# ###
### EFICAS component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
