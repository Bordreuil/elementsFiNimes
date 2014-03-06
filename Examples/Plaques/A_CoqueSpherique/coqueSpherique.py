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


geompy.init_geom(theStudy)

Rcoque = 200.

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(Rcoque, 0, 0)
Sommet_3 = geompy.MakeVertex(0, Rcoque, 0)
Arc_1 = geompy.MakeArcCenter(Sommet_1, Sommet_2, Sommet_3,False)

R_volution_1 = geompy.MakeRevolution(Arc_1, OX, 90*math.pi/180.0)

NZ = geompy.CreateGroup(R_volution_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(NZ, [8])

NY = geompy.CreateGroup(R_volution_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(NY, [9])
NX = geompy.CreateGroup(R_volution_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(NX, [5])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( R_volution_1, 'Révolution_1' )
geompy.addToStudyInFather( R_volution_1, NZ, 'NZ' )
geompy.addToStudyInFather( R_volution_1, NY, 'NY' )
geompy.addToStudyInFather( R_volution_1, NX, 'NX' )

###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import NETGENPlugin
Maillage_1 = smesh.Mesh(R_volution_1)
NETGEN_2D = Maillage_1.Triangle(algo=smesh.NETGEN_1D2D)
NETGEN_2D_Parameters = NETGEN_2D.Parameters()
NETGEN_2D_Parameters.SetMaxSize( 5 )
NETGEN_2D_Parameters.SetSecondOrder( 0 )
NETGEN_2D_Parameters.SetOptimize( 1 )
NETGEN_2D_Parameters.SetFineness( 2 )
NETGEN_2D_Parameters.SetMinSize( 1 )
NETGEN_2D_Parameters.SetQuadAllowed( 0 )
isDone = Maillage_1.Compute()
NZ_1 = Maillage_1.GroupOnGeom(NZ,'NZ',SMESH.NODE)
NY_1 = Maillage_1.GroupOnGeom(NY,'NY',SMESH.NODE)
NX_1 = Maillage_1.GroupOnGeom(NX,'NX',SMESH.NODE)

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(NETGEN_2D.GetAlgorithm(), 'NETGEN_2D')
smesh.SetName(NETGEN_2D_Parameters, 'NETGEN 2D Parameters')
smesh.SetName(NZ_1, 'NZ')
smesh.SetName(NY_1, 'NY')
smesh.SetName(NX_1, 'NX')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
