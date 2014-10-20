# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v7.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)


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
O_1 = geompy.MakeVertex(0, 0, 0)
OX_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeVertex(500, 0, 0)
geomObj_2 = geompy.MakeVertex(0, 500, 0)
geomObj_3 = geompy.MakeVertex(-500, 0, 0)
geomObj_4 = geompy.MakeVertex(0, 500, 0)
Sommet_1 = geompy.MakeVertex(500, 0, 0)
Sommet_2 = geompy.MakeVertex(0, 500, 0)
Sommet_3 = geompy.MakeVertex(-500, 0, 0)
Sommet_4 = geompy.MakeVertex(0, -500, 0)

Arc_1 = geompy.MakeArcCenter(O_1, Sommet_1, Sommet_2,False)
Arc_2 = geompy.MakeArcCenter(O_1, Sommet_2, Sommet_3,False)
Arc_3 = geompy.MakeArcCenter(O_1, Sommet_3, Sommet_4,False)
Arc_4 = geompy.MakeArcCenter(O_1, Sommet_4, Sommet_1,False)

Contour_1 = geompy.MakeWire([Arc_1, Arc_2, Arc_3, Arc_4], 1e-07)
Extrusion_1 = geompy.MakePrismVecH2Ways(Contour_1, OZ, 1000)
Virole = geompy.MakeCompound([Extrusion_1])
[geomObj_5] = geompy.SubShapes(Virole, [11])

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( O_1, 'O' )
geompy.addToStudy( OX_1, 'OX' )
geompy.addToStudy( OY_1, 'OY' )
geompy.addToStudy( OZ_1, 'OZ' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )

geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( Arc_3, 'Arc_3' )
geompy.addToStudy( Arc_4, 'Arc_4' )

geompy.addToStudy( Contour_1, 'Contour_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Virole, 'Virole' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
