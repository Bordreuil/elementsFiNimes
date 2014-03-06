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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/E_BMXPoutre')

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
Sommet_2 = geompy.MakeVertex(0, 0, 100)
Sommet_3 = geompy.MakeVertex(0, 0, 200)
Sommet_4 = geompy.MakeVertex(0, 0, 300)
Sommet_5 = geompy.MakeVertex(-200, 0, 200)
Sommet_6 = geompy.MakeVertex(-200, 0, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_3)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_2)
Ligne_1_vertex_2 = geompy.GetSubShape(Ligne_1, [2])
Cercle_1 = geompy.MakeCircle(Ligne_1_vertex_2, Ligne_1, 70)
Ligne_5_vertex_2 = geompy.GetSubShape(Ligne_5, [2])
Cercle_2 = geompy.MakeCircle(Ligne_5_vertex_2, Ligne_5, 40)
Ligne_4_vertex_2 = geompy.GetSubShape(Ligne_4, [2])
Cercle_3 = geompy.MakeCircle(Ligne_4_vertex_2, Ligne_4, 50)
Contour_1 = geompy.MakeWire([Ligne_1, Ligne_2, Ligne_3], 1e-07)
Tuyau_1 = geompy.MakePipe(Cercle_1, Contour_1)
Tuyau_2 = geompy.MakePipe(Cercle_2, Ligne_5)
Tuyau_3 = geompy.MakePipe(Cercle_3, Ligne_4)
Partition_1 = geompy.MakePartition([Tuyau_1], [Tuyau_2, Tuyau_3], [], [], geompy.ShapeType["SHELL"], 0, [], 0)
[joint,Partition_2,Face_2,Face_1,Face_5,Face_6,Face_7] = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
Partition_2 = geompy.MakePartition([Tuyau_2, Tuyau_3], [Partition_1], [], [], geompy.ShapeType["SHELL"], 0, [], 0)
[Face_1,Face_2,joint,geomObj_1] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
joint = geompy.MakeCompound([Face_5, Face_6, Face_7, Face_1, Face_2])
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
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudyInFather( Ligne_1, Ligne_1_vertex_2, 'Ligne_1:vertex_2' )
geompy.addToStudy( Cercle_1, 'Cercle_1' )
geompy.addToStudyInFather( Ligne_5, Ligne_5_vertex_2, 'Ligne_5:vertex_2' )
geompy.addToStudy( Cercle_2, 'Cercle_2' )
geompy.addToStudyInFather( Ligne_4, Ligne_4_vertex_2, 'Ligne_4:vertex_2' )
geompy.addToStudy( Cercle_3, 'Cercle_3' )
geompy.addToStudy( Contour_1, 'Contour_1' )
geompy.addToStudy( Tuyau_3, 'Tuyau_3' )
geompy.addToStudy( Tuyau_1, 'Tuyau_1' )
geompy.addToStudyInFather( Partition_1, Face_7, 'Face_7' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_2, Face_1, 'Face_1' )
geompy.addToStudyInFather( Partition_2, Face_2, 'Face_2' )
geompy.addToStudy( joint, 'joint' )
geompy.addToStudy( Partition_2, 'Partition_2' )
geompy.addToStudy( Tuyau_2, 'Tuyau_2' )
geompy.addToStudyInFather( Partition_1, Face_5, 'Face_5' )
geompy.addToStudyInFather( Partition_1, Face_6, 'Face_6' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import NETGENPlugin
import StdMeshers
Maillage_1 = smesh.Mesh(joint)
NETGEN_2D = Maillage_1.Triangle(algo=smesh.NETGEN_1D2D)
NETGEN_2D_Simple_Parameters = NETGEN_2D.Parameters(smesh.SIMPLE)
NETGEN_2D_Simple_Parameters.SetNumberOfSegments( 15 )
NETGEN_2D_Simple_Parameters.LengthFromEdges()
NETGEN_2D_Simple_Parameters.SetAllowQuadrangles( 0 )
isDone = Maillage_1.Compute()

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Simple_Parameters, 'NETGEN 2D Simple Parameters_1')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
