# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Soudage/2D')

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
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(500, 0, 0)
Sommet_3 = geompy.MakeVertex(500, 20, 0)
Sommet_4 = geompy.MakeVertex(500, 100, 0)
Sommet_5 = geompy.MakeVertex(0, 100, 0)
Sommet_6 = geompy.MakeVertex(0, 20, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_6)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_6)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_6)
Face_1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
Face_2 = geompy.MakeFaceWires([Ligne_3, Ligne_5, Ligne_6, Ligne_7], 1)
Plaque = geompy.MakeCompound([Face_1, Face_2])
geomObj_1 = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(geomObj_1, [4])
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
Ext = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Ext, [12])
comm = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(comm, [14])
geomObj_2 = geompy.MakeVertex(0, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_4 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_5 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_6 = geompy.MakeVertex(0, 0, 0)
geomObj_7 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_8 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_9 = geompy.MakeVectorDXDYDZ(0, 0, 1)
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
geompy.addToStudyInFather( Plaque, Ext, 'Ext' )
geompy.addToStudyInFather( Plaque, comm, 'comm' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Maillage_1 = smesh.Mesh(Plaque)
NETGEN_2D = Maillage_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetMaxSize( 50 )
NETGEN_2D_Parameters.SetSecondOrder( 0 )
NETGEN_2D_Parameters.SetOptimize( 1 )
NETGEN_2D_Parameters.SetFineness( 2 )
NETGEN_2D_Parameters.SetMinSize( 1 )
NETGEN_2D_Parameters.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters.SetFuseEdges( 1 )
NETGEN_2D_Parameters.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1 = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'NETGENEngine')
NETGEN_2D_Parameters_1.SetMaxSize( 1 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 1 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
status = Maillage_1.AddHypothesis(NETGEN_2D,Fin)
status = Maillage_1.AddHypothesis(NETGEN_2D_Parameters_1,Fin)
Regular_1D = Maillage_1.Segment(geom=comm)
Local_Length_1 = Regular_1D.LocalLength(1,None,1e-07)
isDone = Maillage_1.Compute()
[ Sous_maillage_1, Sous_maillage_2 ] = Maillage_1.GetMesh().GetSubMeshes()
Sous_maillage_1 = Maillage_1.GetSubMesh( Fin, 'Sous-maillage_1' )
Sous_maillage_2 = Regular_1D.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters')
smesh.SetName(Local_Length_1, 'Local Length_1')
smesh.SetName(NETGEN_2D_Parameters, 'NETGEN 2D Parameters')
smesh.SetName(Sous_maillage_1, 'Sous-maillage_1')
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Sous_maillage_2, 'Sous-maillage_2')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
