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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Soudage/2D')

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
Sommet_2 = geompy.MakeVertex(500, 0, 0)
Sommet_3 = geompy.MakeVertex(500, 100, 0)
Sommet_4 = geompy.MakeVertex(0, 100, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
[geomObj_1] = geompy.SubShapeAll(Ligne_1, geompy.ShapeType["EDGE"])
[geomObj_2] = geompy.SubShapeAll(Ligne_1, geompy.ShapeType["EDGE"])
[geomObj_3] = geompy.SubShapeAll(Ligne_1, geompy.ShapeType["EDGE"])
[geomObj_4] = geompy.SubShapeAll(Ligne_1, geompy.ShapeType["EDGE"])
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
[geomObj_5] = geompy.SubShapeAll(Ligne_2, geompy.ShapeType["EDGE"])
[geomObj_6] = geompy.SubShapeAll(Ligne_2, geompy.ShapeType["EDGE"])
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
[geomObj_7] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_8] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_9] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_10] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_11] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_12] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
[geomObj_13] = geompy.SubShapeAll(Ligne_3, geompy.ShapeType["EDGE"])
Ligne_1_vertex_2 = geompy.GetSubShape(Ligne_1, [2])
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_4, Ligne_1_vertex_2)
[geomObj_14] = geompy.SubShapeAll(Ligne_4, geompy.ShapeType["EDGE"])
[geomObj_15] = geompy.SubShapeAll(Ligne_4, geompy.ShapeType["EDGE"])
Face_1 = geompy.MakeFaceWires([Ligne_1, Ligne_2, Ligne_3, Ligne_4], 1)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_1)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_2)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_3)
SymY = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(SymY, [3])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_4)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_7)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_8)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_9)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_10)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_11)
geomObj_16 = geompy.GetInPlace(Face_1, Ligne_3, True)
[geomObj_17] = geompy.SubShapeAll(geomObj_16, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_17)
geomObj_18 = geompy.GetInPlace(Face_1, Ligne_3, True)
[geomObj_19] = geompy.SubShapeAll(geomObj_18, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_19)
geomObj_20 = geompy.GetInPlace(Face_1, Ligne_3, True)
[geomObj_21] = geompy.SubShapeAll(geomObj_20, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_21)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_12)
Bride = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Bride, [8])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_13)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_14)
Debut = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Debut, [10])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_15)
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_5)
Fin = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Fin, [6])
listSameIDs = geompy.GetSameIDs(Face_1, geomObj_6)
Auto_group_for_Sous_maillage_1 = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionList(Auto_group_for_Sous_maillage_1, [Debut, Fin])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudyInFather( Ligne_1, Ligne_1_vertex_2, 'Ligne_1:vertex_2' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudyInFather( Face_1, SymY, 'SymY' )
geompy.addToStudyInFather( Face_1, Bride, 'Bride' )
geompy.addToStudyInFather( Face_1, Debut, 'Debut' )
geompy.addToStudyInFather( Face_1, Fin, 'Fin' )
geompy.addToStudyInFather( Face_1, Auto_group_for_Sous_maillage_1, 'Auto_group_for_Sous-maillage_1' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
import NETGENPlugin
Maillage_1 = smesh.Mesh(Face_1)
Quadrangle_2D = Maillage_1.Quadrangle(algo=smesh.QUADRANGLE)
Quadrangle_Parameters_1 = Quadrangle_2D.QuadrangleParameters(StdMeshers.QUAD_STANDARD)
Regular_1D = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(15)
Nb_Segments_1.SetDistrType( 0 )
status = Maillage_1.RemoveHypothesis(Quadrangle_Parameters_1)
Quadrangle_Parameters_2 = Quadrangle_2D.QuadrangleParameters(StdMeshers.QUAD_QUADRANGLE_PREF)
status = Maillage_1.RemoveHypothesis(Regular_1D)
status = Maillage_1.RemoveHypothesis(Quadrangle_2D)
status = Maillage_1.RemoveHypothesis(Nb_Segments_1)
NETGEN_2D = Maillage_1.Triangle(algo=smesh.NETGEN_1D2D)
status = Maillage_1.RemoveHypothesis(Quadrangle_Parameters_2)
NETGEN_2D_Simple_Parameters = NETGEN_2D.Parameters(smesh.SIMPLE)
NETGEN_2D_Simple_Parameters.SetNumberOfSegments( 15 )
NETGEN_2D_Simple_Parameters.LengthFromEdges()
NETGEN_2D_Simple_Parameters.SetAllowQuadrangles( 0 )
status = Maillage_1.RemoveHypothesis(NETGEN_2D)
Quadrangle_2D_1 = Maillage_1.Quadrangle(algo=smesh.QUADRANGLE)
status = Maillage_1.RemoveHypothesis(NETGEN_2D_Simple_Parameters)
Quadrangle_Parameters_3 = Quadrangle_2D.QuadrangleParameters(StdMeshers.QUAD_STANDARD)
Nb_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
Nb_Segments_2.SetNumberOfSegments( 150 )
Nb_Segments_2.SetDistrType( 0 )
Regular_1D_1 = Maillage_1.Segment()
Nb_Segments_3 = Regular_1D.NumberOfSegments(15)
Regular_1D_2 = Maillage_1.Segment(geom=Auto_group_for_Sous_maillage_1)
Arithmetic_1D_1 = Regular_1D_2.Arithmetic1D(1,6.66667,[  ])
Arithmetic_1D_1.SetObjectEntry( "0:1:1:13" )
status = Maillage_1.RemoveHypothesis(Regular_1D,Auto_group_for_Sous_maillage_1)
status = Maillage_1.RemoveHypothesis(Arithmetic_1D_1,Auto_group_for_Sous_maillage_1)
Regular_1D_3 = Maillage_1.Segment(geom=Debut)
Arithmetic_1D_2 = Regular_1D_3.Arithmetic1D(50.9902,1,[  ])
Regular_1D_4 = Maillage_1.Segment(geom=Fin)
Arithmetic_1D_3 = Regular_1D_4.Arithmetic1D(1,50.9902,[  ])
Arithmetic_1D_3.SetStartLength( 1 )
Arithmetic_1D_3.SetEndLength( 10 )
Arithmetic_1D_3.SetReversedEdges( [  ] )
Arithmetic_1D_3.SetObjectEntry( "0:1:1:13" )
Arithmetic_1D_2.SetStartLength( 10 )
Arithmetic_1D_2.SetEndLength( 1 )
Arithmetic_1D_2.SetReversedEdges( [  ] )
Arithmetic_1D_2.SetObjectEntry( "0:1:1:13" )
Nb_Segments_3.SetNumberOfSegments( 40 )
Nb_Segments_3.SetDistrType( 0 )
isDone = Maillage_1.Compute()
SymY_1 = Maillage_1.GroupOnGeom(SymY,'SymY',SMESH.NODE)
Bride_1 = Maillage_1.GroupOnGeom(Bride,'Bride',SMESH.NODE)
#Maillage_1.RemoveGroup( smeshObj_1 ) ### smeshObj_1 has not been yet created
TOUT = Maillage_1.GroupOnGeom(Face_1,'Face_1',SMESH.FACE)
TOUT.SetName( 'TOUT' )
Sous_maillage_1 = Regular_1D_3.GetSubMesh()
Sous_maillage_2 = Regular_1D_4.GetSubMesh()

## some objects were removed
aStudyBuilder = theStudy.NewBuilder()
SO = theStudy.FindObjectIOR(theStudy.ConvertObjectToIOR(smeshObj_1))
if SO is not None: aStudyBuilder.RemoveObjectWithChildren(SO)
## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Quadrangle_Parameters_2, 'Quadrangle Parameters_2')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Simple_Parameters, 'NETGEN 2D Simple Parameters_1')
smesh.SetName(Quadrangle_Parameters_3, 'Quadrangle Parameters_3')
smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
smesh.SetName(Nb_Segments_3, 'Nb. Segments_3')
smesh.SetName(Arithmetic_1D_1, 'Arithmetic 1D_1')
smesh.SetName(Arithmetic_1D_2, 'Arithmetic 1D_2')
smesh.SetName(Arithmetic_1D_3, 'Arithmetic 1D_3')
smesh.SetName(SymY_1, 'SymY')
smesh.SetName(Bride_1, 'Bride')
smesh.SetName(TOUT, 'TOUT')
smesh.SetName(Sous_maillage_1, 'Sous-maillage_1')
smesh.SetName(Sous_maillage_2, 'Sous-maillage_2')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
