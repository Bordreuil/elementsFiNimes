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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Poutres/D_Treillis')

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
Sommet_2 = geompy.MakeVertex(2000, 0, 0)
Sommet_3 = geompy.MakeVertex(4000, 0, 0)
Sommet_4 = geompy.MakeVertex(6000, 0, 0)
Sommet_5 = geompy.MakeVertex(1000, 1500, 0)
Sommet_6 = geompy.MakeVertex(3000, 1500, 0)
Sommet_7 = geompy.MakeVertex(5000, 1500, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_7)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_3)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_6)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_2)
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_5)
Ligne_1_vertex_2 = geompy.GetSubShape(Ligne_1, [2])
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_5, Ligne_1_vertex_2)
Ligne_8_vertex_3 = geompy.GetSubShape(Ligne_8, [3])
Ligne_10 = geompy.MakeLineTwoPnt(Ligne_8_vertex_3, Sommet_6)
Ligne_11 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_7)
Treillis = geompy.MakeCompound([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Ligne_5, Ligne_6, Ligne_7, Ligne_8, Ligne_9, Ligne_10, Ligne_11])
listSubShapeIDs = geompy.SubShapeAllIDs(Treillis, geompy.ShapeType["SHAPE"])
geomObj_1 = geompy.GetSubShape(Treillis, [2])
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
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudy( Ligne_8, 'Ligne_8' )
geompy.addToStudy( Ligne_9, 'Ligne_9' )
geompy.addToStudyInFather( Ligne_1, Ligne_1_vertex_2, 'Ligne_1:vertex_2' )
geompy.addToStudyInFather( Ligne_8, Ligne_8_vertex_3, 'Ligne_8:vertex_3' )
geompy.addToStudy( Ligne_10, 'Ligne_10' )
geompy.addToStudy( Ligne_11, 'Ligne_11' )
geompy.addToStudy( Treillis, 'Treillis' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Maillage_1 = smesh.Mesh(Treillis)
Regular_1D = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(1)
Nb_Segments_1.SetDistrType( 0 )

isDone = Maillage_1.Compute()
Treillis_1 = Maillage_1.GroupOnGeom(Treillis,'Treillis',SMESH.EDGE)
Liaison = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Liaison' )
nbAdd = Liaison.Add( [ 1, 4 ] )
Efforts = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Efforts' )
nbAdd = Efforts.Add( [ 2, 3 ] )
isDone = Maillage_1.Compute()
## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Treillis_1, 'Treillis')
smesh.SetName(Liaison, 'Liaison')
smesh.SetName(Efforts, 'Efforts')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
