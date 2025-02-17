#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.9.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/bordreuil/Enseignement/elementsFiNimes/Projets/Cloche')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(25, 0, 0)
Sommet_3 = geompy.MakeVertex(25, 10, 0)
Sommet_4 = geompy.MakeVertex(50, 100, 0)
Sommet_5 = geompy.MakeVertex(15, 10, 0)
Sommet_6 = geompy.MakeVertex(15, 0, 0)
Sommet_7 = geompy.MakeVertex(40, 100, 0)
Sommet_8 = geompy.MakeVertex(0, 10, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_7)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_5)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_8)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_1)
Face_1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Ligne_5, Ligne_6, Ligne_7], 1)
R__volution_1 = geompy.MakeRevolution(Face_1, OY, 360*math.pi/180.0)
Enc = geompy.CreateGroup(R__volution_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Enc, [3])
[Enc] = geompy.GetExistingSubObjects(R__volution_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( R__volution_1, 'Révolution_1' )
geompy.addToStudyInFather( R__volution_1, Enc, 'Enc' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Maillage_1 = smesh.Mesh(R__volution_1,'Maillage_1')
NETGEN_1D_2D_3D = Maillage_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 20 )
NETGEN_3D_Parameters_1.SetMinSize( 3 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetChordalError( -1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
Enc_1 = Maillage_1.GroupOnGeom(Enc,'Enc',SMESH.FACE)
isDone = Maillage_1.Compute()
[ Enc_1 ] = Maillage_1.GetGroups()
NETGEN_3D_Parameters_1.SetMaxSize( 10 )
NETGEN_3D_Parameters_1.SetMinSize( 2 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
isDone = Maillage_1.Compute()
[ Enc_1 ] = Maillage_1.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Enc_1, 'Enc')
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
