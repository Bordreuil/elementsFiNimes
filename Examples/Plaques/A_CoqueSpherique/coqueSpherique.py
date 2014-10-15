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
import math
import SALOMEDS
from salome.geom import geomBuilder

geompy = geomBuilder.New(salome.myStudy)


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
geompy.addToStudy( R_volution_1, 'Coque' )
geompy.addToStudyInFather( R_volution_1, NZ, 'NZ' )
geompy.addToStudyInFather( R_volution_1, NY, 'NY' )
geompy.addToStudyInFather( R_volution_1, NX, 'NX' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
