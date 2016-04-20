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

Lplq  =  500.
lplq  =  100.
lfin  =  20.

geompy.init_geom(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(Lplq, 0, 0)
Sommet_3 = geompy.MakeVertex(Lplq, lfin, 0)
Sommet_4 = geompy.MakeVertex(Lplq, lplq, 0)
Sommet_5 = geompy.MakeVertex(0,lplq,0)
Sommet_6 = geompy.MakeVertex(0,lfin,0)

Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_6)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_6)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_3,Sommet_4)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_4,Sommet_5)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_5,Sommet_6)
Face_1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
Face_2 = geompy.MakeFaceWires([Ligne_3, Ligne_5, Ligne_6, Ligne_7], 1)
Plaque = geompy.MakeCompound([Face_1, Face_2])
Sym = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Sym, [4])
gauche = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(gauche, [7])
droite = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(droite, [11])
Fin = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Fin, [2])
centre = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(centre, [4, 9])
ext = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(ext, [19])

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
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )

geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, gauche, 'gauche' )
geompy.addToStudyInFather( Plaque, droite, 'droite' )
geompy.addToStudyInFather( Plaque, Fin, 'Fin' )
geompy.addToStudyInFather( Plaque, centre, 'centre' )
geompy.addToStudyInFather( Plaque, ext, 'ext' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
import NETGENPlugin

Maillage_1 = smesh.Mesh(Plaque)
NETGEN_2D = Maillage_1.Triangle(algo=smesh.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetMaxSize( 50 )
NETGEN_2D_Parameters.SetSecondOrder( 0 )
NETGEN_2D_Parameters.SetOptimize( 1 )
NETGEN_2D_Parameters.SetFineness( 2 )
NETGEN_2D_Parameters.SetMinSize( 1 )
NETGEN_2D_Parameters.SetQuadAllowed( 0 )
Regular_1D = Maillage_1.Segment(geom=centre)
Nb_Segments_1 = Regular_1D.NumberOfSegments(250)
Nb_Segments_1.SetDistrType( 0 )
Regular_1D_1 = Maillage_1.Segment(geom=gauche)
Arithmetic_1D_1 = Regular_1D_1.Arithmetic1D(1,5,[  ])
Regular_1D_2 = Maillage_1.Segment(geom=droite)
Arithmetic_1D_2 = Regular_1D_2.Arithmetic1D(1,5,[  ])
Regular_1D_3 = Maillage_1.Segment(geom=ext)
Nb_Segments_2 = Regular_1D_3.NumberOfSegments(50)
Nb_Segments_2.SetDistrType( 0 )
Quadrangle_2D = Maillage_1.Quadrangle(algo=smesh.QUADRANGLE,geom=Fin)
Quadrangle_Parameters_1 = Quadrangle_2D.QuadrangleParameters(StdMeshers.QUAD_STANDARD)
Arithmetic_1D_2.SetStartLength( 1 )
Arithmetic_1D_2.SetEndLength( 1 )
Arithmetic_1D_2.SetReversedEdges( [  ] )
Arithmetic_1D_2.SetObjectEntry( "0:1:1:24" )
Arithmetic_1D_1.SetStartLength( 1 )
Arithmetic_1D_1.SetEndLength( 1 )
Arithmetic_1D_1.SetReversedEdges( [  ] )
Arithmetic_1D_1.SetObjectEntry( "0:1:1:24" )
isDone = Maillage_1.Compute()
Sous_maillage_1 = Regular_1D.GetSubMesh()
Sous_maillage_2 = Regular_1D_1.GetSubMesh()
Sous_maillage_3 = Regular_1D_2.GetSubMesh()
Sous_maillage_4 = Regular_1D_3.GetSubMesh()
Sous_maillage_5 = Quadrangle_2D.GetSubMesh()

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Parameters, 'NETGEN 2D Parameters')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Arithmetic_1D_1, 'Arithmetic 1D_1')
smesh.SetName(Arithmetic_1D_2, 'Arithmetic 1D_2')
smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Sous_maillage_1, 'Sous-maillage_1')
smesh.SetName(Sous_maillage_2, 'Sous-maillage_2')
smesh.SetName(Sous_maillage_3, 'Sous-maillage_3')
smesh.SetName(Sous_maillage_4, 'Sous-maillage_4')
smesh.SetName(Sous_maillage_5, 'Sous-maillage_5')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
