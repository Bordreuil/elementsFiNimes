#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
#sys.path.insert(0, r'/home/bordreuil/homedebian/home/bordreuil/Enseignement/elementsFiNimes/Examples/Soudage/3D')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy    = geomBuilder.New()

O          = geompy.MakeVertex(0, 0, 0)
OX         = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY         = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ         = geompy.MakeVectorDXDYDZ(0, 0, 1)
zFin       = 5
ep         = 10
zTran      = 10
lar        = 100
L          = 200
Sommet_1   = geompy.MakeVertex(0, 0, 0)
Sommet_2   = geompy.MakeVertex(zFin, 0, 0)
Sommet_3   = geompy.MakeVertex(zFin, -zFin, 0)
Sommet_4   = geompy.MakeVertex(0, -zFin, 0)
Sommet_5   = geompy.MakeVertex(0, -ep, 0)
Sommet_6   = geompy.MakeVertex(zTran, -ep, 0)
Sommet_7   = geompy.MakeVertex(zTran, 0, 0)
Sommet_8   = geompy.MakeVertex(lar, 0, 0)
Sommet_9   = geompy.MakeVertex(lar, -ep, 0)
Ligne_1    = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Ligne_2    = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_3    = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Ligne_4    = geompy.MakeLineTwoPnt(Sommet_4, Sommet_1)
Ligne_5    = geompy.MakeLineTwoPnt(Sommet_2, Sommet_7)
Ligne_6    = geompy.MakeLineTwoPnt(Sommet_7, Sommet_6)
Ligne_7    = geompy.MakeLineTwoPnt(Sommet_3, Sommet_6)
Ligne_8    = geompy.MakeLineTwoPnt(Sommet_6, Sommet_5)
Ligne_9    = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Ligne_10   = geompy.MakeLineTwoPnt(Sommet_7, Sommet_8)
Ligne_11   = geompy.MakeLineTwoPnt(Sommet_8, Sommet_9)
Ligne_12   = geompy.MakeLineTwoPnt(Sommet_6, Sommet_9)
geomObj_1  = geompy.MakeFaceWires([Ligne_4, Ligne_3, Ligne_2, Ligne_1], 1)
Face_1     = geompy.ChangeOrientationShellCopy(geomObj_1)
Face_2     = geompy.MakeFaceWires([Ligne_2, Ligne_5, Ligne_6, Ligne_7], 1)
Face_3     = geompy.MakeFaceWires([Ligne_3, Ligne_7, Ligne_8, Ligne_9], 1)
Face_4     = geompy.MakeFaceWires([Ligne_6, Ligne_10, Ligne_11, Ligne_12], 1)
Section    = geompy.MakeCompound([Face_1, Face_2, Face_3, Face_4])
Partition_1= geompy.MakePartition([Section], [Section], [], [], geompy.ShapeType["FACE"], 0, [], 0)
epa        = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(epa, [11, 16, 28, 7])
fond       = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fond, [23, 4, 9])
lar        = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(lar, [26, 30])
ctr        = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(ctr, [14, 18, 21])
Plaque     = geompy.MakePrismVecH(Partition_1, OZ, L)
epa_1      = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(epa_1, [51, 92, 27, 13, 26, 91, 50, 12])
fond_1     = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fond_1, [95, 84, 96, 85])
extru      = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(extru, [16, 64, 47, 9, 88, 6, 81, 23, 40])
finm       = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(finm, [30, 19, 71, 72, 20, 31])
ctr_1      = geompy.CreateGroup(Plaque, geompy.ShapeType["EDGE"])
geompy.UnionIDs(ctr_1, [44, 54, 55, 67, 43, 68])
Sym        = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Sym, [4, 62])
BordB      = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(BordB, [75, 58, 99, 34])
Haut       = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Haut, [14, 52, 93])
Bas        = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Bas, [69, 79])
BordH      = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(BordH, [56, 73, 32, 97])
CoteE      = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(CoteE, [86])
Soud       = geompy.CreateGroup(Plaque, geompy.ShapeType["FACE"])
geompy.UnionIDs(Soud, [14])

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
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudy( Face_4, 'Face_4' )
geompy.addToStudy( Section, 'Section' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, epa, 'epa' )
geompy.addToStudyInFather( Partition_1, fond, 'fond' )
geompy.addToStudyInFather( Partition_1, lar, 'lar' )
geompy.addToStudyInFather( Partition_1, ctr, 'ctr' )
geompy.addToStudy( Plaque, 'Plaque' )
geompy.addToStudyInFather( Plaque, epa_1, 'epa' )
geompy.addToStudyInFather( Plaque, fond_1, 'fond' )
geompy.addToStudyInFather( Plaque, extru, 'extru' )
geompy.addToStudyInFather( Plaque, finm, 'finm' )
geompy.addToStudyInFather( Plaque, ctr_1, 'ctr' )
geompy.addToStudyInFather( Plaque, Sym, 'Sym' )
geompy.addToStudyInFather( Plaque, BordB, 'BordB' )
geompy.addToStudyInFather( Plaque, Haut, 'Haut' )
geompy.addToStudyInFather( Plaque, Bas, 'Bas' )
geompy.addToStudyInFather( Plaque, BordH, 'BordH' )
geompy.addToStudyInFather( Plaque, CoteE, 'CoteE' )
geompy.addToStudyInFather( Plaque, Soud, 'Soud' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Maillage_2              = smesh.Mesh(Plaque)
Regular_1D_5            = Maillage_2.Segment()
Local_Length_2          = Regular_1D_5.LocalLength(2,None,1e-07)
Quadrangle_2D_1         = Maillage_2.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_Parameters_1 = Quadrangle_2D_1.QuadrangleParameters(smeshBuilder.QUAD_STANDARD,-1,[],[])
status                  = Maillage_2.AddHypothesis(Quadrangle_Parameters_1)
Hexa_3D                 = Maillage_2.Hexahedron(algo=smeshBuilder.Hexa)
Regular_1D_6            = Maillage_2.Segment(geom=epa_1)
Number_of_Segments_4    = Regular_1D_6.NumberOfSegments(10)
Regular_1D_7            = Maillage_2.Segment(geom=extru)
Local_Length_3          = Regular_1D_7.LocalLength(2,None,1e-07)
Regular_1D_8            = Maillage_2.Segment(geom=ctr_1)
Number_of_Segments_5    = Regular_1D_8.NumberOfSegments(10)
Regular_1D_9            = Maillage_2.Segment(geom=finm)
status                  = Maillage_2.AddHypothesis(Number_of_Segments_5,finm)
Regular_1D_10           = Maillage_2.Segment(geom=fond_1)
Start_and_End_Length_1  = Regular_1D_10.StartEndLength(2,20,[])
Start_and_End_Length_1.SetObjectEntry( "Plaque" )
isDone                  = Maillage_2.Compute()
Sym_1                   = Maillage_2.GroupOnGeom(Sym,'Sym',SMESH.FACE)
BordB_1                 = Maillage_2.GroupOnGeom(BordB,'BordB',SMESH.FACE)
Haut_1                  = Maillage_2.GroupOnGeom(Haut,'Haut',SMESH.FACE)
Bas_1                   = Maillage_2.GroupOnGeom(Bas,'Bas',SMESH.FACE)
BordH_1                 = Maillage_2.GroupOnGeom(BordH,'BordH',SMESH.FACE)
CoteE_1                 = Maillage_2.GroupOnGeom(CoteE,'CoteE',SMESH.FACE)
smesh.SetName(Maillage_2, 'Maillage_2')

Soud_1          = Maillage_2.GroupOnGeom(Soud,'Soud',SMESH.FACE)

Sous_maillage_5 = Regular_1D_6.GetSubMesh()
Sous_maillage_6 = Regular_1D_7.GetSubMesh()
Sous_maillage_7 = Regular_1D_8.GetSubMesh()
Sous_maillage_8 = Regular_1D_9.GetSubMesh()
Sous_maillage_9 = Regular_1D_10.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Quadrangle_2D_1.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Sous_maillage_8, 'Sous-maillage_8')
smesh.SetName(Local_Length_2, 'Local Length_2')
smesh.SetName(Sous_maillage_9, 'Sous-maillage_9')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Sous_maillage_5, 'Sous-maillage_5')
smesh.SetName(Sous_maillage_6, 'Sous-maillage_6')
smesh.SetName(Sous_maillage_7, 'Sous-maillage_7')
smesh.SetName(Maillage_2.GetMesh(), 'Maillage_2')
smesh.SetName(Start_and_End_Length_1, 'Start and End Length_1')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(Local_Length_3, 'Local Length_3')
smesh.SetName(Soud_1, 'Soud')
smesh.SetName(CoteE_1, 'CoteE')
smesh.SetName(BordH_1, 'BordH')
smesh.SetName(Bas_1, 'Bas')
smesh.SetName(Haut_1, 'Haut')
smesh.SetName(BordB_1, 'BordB')
smesh.SetName(Sym_1, 'Sym')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
