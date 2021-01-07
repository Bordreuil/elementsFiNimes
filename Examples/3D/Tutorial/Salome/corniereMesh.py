# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/bordreuil/homedebian/home/bordreuil/Enseignement/elementsFiNimes/Examples/3D/Tutorial/Salome')

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
Sommet_1 = geompy.MakeVertex(-100, 0, 0)
Sommet_2 = geompy.MakeVertex(-100, 10, 0)
Sommet_3 = geompy.MakeVertex(-10, 10, 0)
Sommet_4 = geompy.MakeVertex(-10, 100, 0)
Sommet_5 = geompy.MakeVertex(0, 100, 0)
Sommet_6 = geompy.MakeVertex(0, 0, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_6)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_1)
Section = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Ligne_5, Ligne_6], 1)
Corniere = geompy.MakePrismVecH(Section, OZ, 1000)
Encastre = geompy.CreateGroup(Corniere, geompy.ShapeType["FACE"])
geompy.UnionIDs(Encastre, [45])
Force = geompy.CreateGroup(Corniere, geompy.ShapeType["FACE"])
geompy.UnionIDs(Force, [47])
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
geompy.addToStudy( Section, 'Section' )
geompy.addToStudy( Corniere, 'Corniere' )
geompy.addToStudyInFather( Corniere, Encastre, 'Encastre' )
geompy.addToStudyInFather( Corniere, Force, 'Force' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Maillage_1 = smesh.Mesh(Corniere)
NETGEN_1D_2D_3D = Maillage_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 20 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetChordalError( 0.1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetMinSize( 5 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
isDone = Maillage_1.Compute()
Encastre_1 = Maillage_1.GroupOnGeom(Encastre,'Encastre',SMESH.FACE)
Force_1 = Maillage_1.GroupOnGeom(Force,'Force',SMESH.FACE)
Encastre_2 = Maillage_1.GroupOnGeom(Encastre,'Encastre',SMESH.NODE)
Force_2 = Maillage_1.GroupOnGeom(Force,'Force',SMESH.NODE)


## Set names of Mesh objects
smesh.SetName(Force_2, 'Force')
smesh.SetName(Encastre_2, 'Encastre')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(Encastre_1, 'Encastre')
smesh.SetName(Force_1, 'Force')
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')

###
### ASTERSTUDY component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
