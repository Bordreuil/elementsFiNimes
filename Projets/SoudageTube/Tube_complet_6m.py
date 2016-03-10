# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v7.4.0 with dump python functionality
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
import math
import SALOMEDS
from salome.geom import geomBuilder
geompy = geomBuilder.New(theStudy)

###
### Données d'entrés
###

#Diamètre du tube

D_ext = 406.4 ;
Epaisseur = 12.7;
L_tube = 6000 ;
L_fin= 20 ;

### 
### Modélisation
###

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex( (D_ext/2) , 0, (L_fin) )
Sommet_2 = geompy.MakeVertex( ((D_ext/2)-Epaisseur) , 0, (L_fin) )
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_1)
R_volution_1 = geompy.MakeRevolution(Ligne_1, OZ, 90*math.pi/180.0)

Tube_fin = geompy.MakePrismVecH(R_volution_1, OZ, (-L_fin))
[Epais1] = geompy.SubShapes(Tube_fin, [29])
[Epais2] = geompy.SubShapes(Tube_fin, [25])
[Epais3] = geompy.SubShapes(Tube_fin, [30])
[Epais4] = geompy.SubShapes(Tube_fin, [26])
[Arc1] = geompy.SubShapes(Tube_fin, [11])
[Arc2] = geompy.SubShapes(Tube_fin, [21])
[Arc3] = geompy.SubShapes(Tube_fin, [12])
[Arc4] = geompy.SubShapes(Tube_fin, [22])
[Sym1] = geompy.SubShapes(Tube_fin, [33])
Tube_gros = geompy.MakePrismVecH(R_volution_1, OZ, (L_tube-L_fin))
[Epais5] = geompy.SubShapes(Tube_gros, [25])
[Epais6] = geompy.SubShapes(Tube_gros, [29])
[Epais7] = geompy.SubShapes(Tube_gros, [26])
[Epais8] = geompy.SubShapes(Tube_gros, [30])
[Arc5] = geompy.SubShapes(Tube_gros, [21])
[Arc6] = geompy.SubShapes(Tube_gros, [11])
[Arc7] = geompy.SubShapes(Tube_gros, [22])
[Arc8] = geompy.SubShapes(Tube_gros, [12])

Epais = geompy.CreateGroup(Tube_fin, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Epais, [29, 25, 30, 26])
Arc = geompy.CreateGroup(Tube_fin, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Arc, [11, 21, 12, 22])
Epais_gros = geompy.CreateGroup(Tube_gros, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Epais_gros, [25, 29, 26, 30])
Arc_gros = geompy.CreateGroup(Tube_gros, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Arc_gros, [21, 11, 22, 12])
Tube = geompy.MakeCompound([Tube_fin, Tube_gros])

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( R_volution_1, 'R_volution_1' )
geompy.addToStudy( Tube_fin, 'Tube_fin' )
geompy.addToStudy( Tube_gros, 'Tube_gros' )
geompy.addToStudyInFather( Tube_fin, Epais1, 'Epais1' )
geompy.addToStudyInFather( Tube_fin, Epais2, 'Epais2' )
geompy.addToStudyInFather( Tube_fin, Epais3, 'Epais3' )
geompy.addToStudyInFather( Tube_fin, Epais4, 'Epais4' )
geompy.addToStudyInFather( Tube_fin, Arc1, 'Arc1' )
geompy.addToStudyInFather( Tube_fin, Arc2, 'Arc2' )
geompy.addToStudyInFather( Tube_fin, Arc3, 'Arc3' )
geompy.addToStudyInFather( Tube_fin, Arc4, 'Arc4' )
geompy.addToStudyInFather( Tube_fin, Sym1, 'Sym1' )
geompy.addToStudyInFather( Tube_fin, Epais, 'Epais' )
geompy.addToStudyInFather( Tube_fin, Arc, 'Arc' )
geompy.addToStudyInFather( Tube_gros, Epais5, 'Epais5' )
geompy.addToStudyInFather( Tube_gros, Epais6, 'Epais6' )
geompy.addToStudyInFather( Tube_gros, Epais7, 'Epais7' )
geompy.addToStudyInFather( Tube_gros, Epais8, 'Epais8' )
geompy.addToStudyInFather( Tube_gros, Arc5, 'Arc5' )
geompy.addToStudyInFather( Tube_gros, Arc6, 'Arc6' )
geompy.addToStudyInFather( Tube_gros, Arc7, 'Arc7' )
geompy.addToStudyInFather( Tube_gros, Arc8, 'Arc8' )
geompy.addToStudyInFather( Tube_gros, Epais_gros, 'Epais_gros' )
geompy.addToStudyInFather( Tube_gros, Arc_gros, 'Arc_gros' )
geompy.addToStudy( Tube, 'Tube' )
[from_Tube_fin, from_Epais1, from_Epais2, from_Epais3, from_Epais4, from_Arc1, from_Arc2, from_Arc3, from_Arc4, from_Sym1, from_Epais, from_Arc, from_Tube_gros, from_Epais5, from_Epais6, from_Epais7, from_Epais8, from_Arc5, from_Arc6, from_Arc7, from_Arc8, from_Epais_gros, from_Arc_gros] = geompy.RestoreGivenSubShapes(Tube, [Tube_fin, Epais1, Epais2, Epais3, Epais4, Arc1, Arc2, Arc3, Arc4, Sym1, Epais, Arc, Tube_gros, Epais5, Epais6, Epais7, Epais8, Arc5, Arc6, Arc7, Arc8, Epais_gros, Arc_gros], GEOM.FSM_GetInPlace, False, True)

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Maillage_1 = smesh.Mesh(Tube)
NETGEN_2D3D = Maillage_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters = NETGEN_2D3D.Parameters()
NETGEN_3D_Parameters.SetMaxSize( 30 )
NETGEN_3D_Parameters.SetSecondOrder( 0 )
NETGEN_3D_Parameters.SetOptimize( 1 )
NETGEN_3D_Parameters.SetFineness( 2 )
NETGEN_3D_Parameters.SetMinSize( 20 )
NETGEN_3D_Parameters.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters.SetFuseEdges( 1 )
NETGEN_3D_Parameters.SetQuadAllowed( 0 )
Regular_1D = Maillage_1.Segment(geom=from_Tube_fin)
Sous_maillage_1 = Regular_1D.GetSubMesh()
Local_Length_1 = Regular_1D.LocalLength(2,[],1e-07)
Quadrangle_2D = Maillage_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=from_Tube_fin)
Hexa_3D = Maillage_1.Hexahedron(algo=smeshBuilder.Hexa,geom=from_Tube_fin)
Nb_Segments_1 = smesh.CreateHypothesis('NumberOfSegments')
Nb_Segments_1.SetNumberOfSegments( 24 )
Nb_Segments_1.SetDistrType( 0 )
Sous_maillage_2 = Maillage_1.GetSubMesh( from_Epais, 'Sous-maillage_2' )
status = Maillage_1.AddHypothesis(Regular_1D,from_Epais)
status = Maillage_1.AddHypothesis(Nb_Segments_1,from_Epais)
isDone = Maillage_1.SetMeshOrder( [ [ Sous_maillage_2, Sous_maillage_1 ] ])
Nb_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
Nb_Segments_2.SetNumberOfSegments( 480 )
Nb_Segments_2.SetDistrType( 0 )
Sous_maillage_3 = Maillage_1.GetSubMesh( from_Arc, 'Sous-maillage_3' )
status = Maillage_1.AddHypothesis(Regular_1D,from_Arc)
status = Maillage_1.AddHypothesis(Nb_Segments_2,from_Arc)
isDone = Maillage_1.SetMeshOrder( [ [ Sous_maillage_2, Sous_maillage_3, Sous_maillage_1 ] ])
isDone = Maillage_1.Compute()
[ Sous_maillage_1, Sous_maillage_2, Sous_maillage_3 ] = Maillage_1.GetMesh().GetSubMeshes()
Sym1_1 = Maillage_1.GroupOnGeom(from_Tube_fin,'from_Tube_fin',SMESH.VOLUME)
Sym1_1.SetName( 'Sym1' )
[ Sym1_mirrored ] = Maillage_1.MirrorObject( Maillage_1, SMESH.AxisStruct( 0, 0, 0, 1, 0, 0 ), SMESH.SMESH_MeshEditor.PLANE ,True,True)
[ Sym1_mirrored_1, Sym1_mirrored_mirrored ] = Maillage_1.MirrorObject( Maillage_1, SMESH.AxisStruct( 0, 0, 0, 0, -1, 0 ), SMESH.SMESH_MeshEditor.PLANE ,True,True)

# Merging Nodes
mesh = Maillage_1
Tolerance = 1e-5
GroupsOfNodes = mesh.FindCoincidentNodes(Tolerance)
mesh.MergeNodes(GroupsOfNodes) 
# Merging Elements
equal_elements = Maillage_1.FindEqualElements( Maillage_1 )
Maillage_1.MergeElements(equal_elements)
Sym = Maillage_1.GetMesh().UnionListOfGroups([ Sym1_1, Sym1_mirrored, Sym1_mirrored_1, Sym1_mirrored_mirrored ], 'Sym' )
Sym.SetColor( SALOMEDS.Color( 1, 0, 0 ))

# Passage au quadratique
Maillage_1.ConvertToQuadratic(1)

## Set names of Mesh objects
smesh.SetName(NETGEN_2D3D.GetAlgorithm(), 'NETGEN_2D3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Local_Length_1, 'Local Length_1')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(NETGEN_3D_Parameters, 'NETGEN 3D Parameters')
smesh.SetName(Nb_Segments_2, 'Nb. Segments_2')
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Sous_maillage_3, 'Sous-maillage_3')
smesh.SetName(Sous_maillage_2, 'Sous-maillage_2')
smesh.SetName(Sous_maillage_1, 'Sous-maillage_1')
smesh.SetName(Sym1_mirrored_mirrored, 'Sym1_mirrored_mirrored')
smesh.SetName(Sym1_mirrored_1, 'Sym1_mirrored_1')
smesh.SetName(Sym1_mirrored, 'Sym1_mirrored')
smesh.SetName(Sym1_1, 'Sym1')
smesh.SetName(Sous_maillage_1, 'Sous-maillage_1')
smesh.SetName(Sym, 'Sym')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
