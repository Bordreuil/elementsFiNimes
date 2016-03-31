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
#sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Projets/Marathon2016')

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

lFixInt  = 90.
lEco     = 250.
LArrRenf = 363.
LArrRoue = 620.
LAvRenf  = 140.
LAvAxe   = 910.
LAvRoue  = 1070.
lAvAxe   = 225.
ZPlat    = 120.
ZArceau  = ZPlat+lEco     
Sommet_1 = geompy.MakeVertex(0, 0, 0)
Sommet_2 = geompy.MakeVertex(lFixInt, 0, 0)
Sommet_3 = geompy.MakeVertex(lEco, 0, 0)
Sommet_4 = geompy.MakeVertex(-lFixInt, 0, 0)
Sommet_5 = geompy.MakeVertex(-lEco, 0, 0)
Sommet_6 = geompy.MakeVertex(lFixInt, -LArrRenf, 0)
Sommet_7 = geompy.MakeVertex(-lFixInt, -LArrRenf, 0)
Sommet_8 = geompy.MakeVertex(-lFixInt, -LArrRoue, 0)
Sommet_9 = geompy.MakeVertex(lFixInt, -LArrRoue, 0)
Sommet_10 = geompy.MakeVertex(0, LAvRenf, 0)
Sommet_11 = geompy.MakeVertex(0, LAvAxe, 0)
Sommet_12 = geompy.MakeVertex(0, LAvRoue, 0)
Sommet_13 = geompy.MakeVertex(lAvAxe, LAvAxe, 0)
Sommet_14 = geompy.MakeVertex(-lAvAxe, LAvAxe, 0)
Sommet_15 = geompy.MakeVertex(0, 0, ZPlat)
Sommet_16 = geompy.MakeVertex(lEco, 0, ZPlat)
Sommet_17 = geompy.MakeVertex(-lEco, 0, ZPlat)
Sommet_18 = geompy.MakeVertex(0, 0, ZArceau)

geomObj_1 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_8)
geomObj_2 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_2)
geomObj_3 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_3)
geomObj_4 = geompy.MakeLineTwoPnt(Sommet_1, Sommet_12)
geomObj_5 = geompy.MakeLineTwoPnt(Sommet_14, Sommet_13)

geomObj_6 = geompy.GetSubShape(geomObj_3, [2])
geomObj_7 = geompy.MakeLineTwoPnt(geomObj_6, Sommet_17)
geomObj_8 = geompy.GetSubShape(geomObj_3, [3])
geomObj_9 = geompy.MakeLineTwoPnt(geomObj_8, Sommet_16)
geomObj_10 = geompy.GetSubShape(geomObj_7, [3])
geomObj_11 = geompy.GetSubShape(geomObj_7, [3])
geomObj_12 = geompy.GetSubShape(geomObj_7, [3])
geomObj_13 = geompy.GetSubShape(geomObj_7, [3])
geomObj_14 = geompy.GetSubShape(geomObj_7, [3])
geomObj_15 = geompy.GetSubShape(geomObj_7, [3])

geomObj_16 = geompy.MakeArc(Sommet_16, Sommet_18, geomObj_15)
geomObj_17 = geompy.MakeLineTwoPnt(Sommet_18, Sommet_10)
geomObj_18 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_7)
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_4)
OX_vertex_3 = geompy.GetSubShape(OX, [3])
Ligne_3 = geompy.MakeLineTwoPnt(Sommet_4, OX_vertex_3)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_6)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_2)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Ligne_7 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_12, Sommet_11)
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_11, Sommet_10)
Ligne_10 = geompy.MakeLineTwoPnt(Sommet_10, OX_vertex_3)
Ligne_11 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_17)
Ligne_12 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_16)
Ligne_13 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_1)
Ligne_14 = geompy.MakeLineTwoPnt(Sommet_11, Sommet_14)
Ligne_15 = geompy.MakeLineTwoPnt(Sommet_11, Sommet_13)
Ligne_16 = geompy.MakeLineTwoPnt(Sommet_10, Sommet_18)
Arc_1 = geompy.MakeArcCenter(Sommet_15, Sommet_17, Sommet_18,False)
Arc_2 = geompy.MakeArcCenter(Sommet_15, Sommet_18, Sommet_16,False)
Chassis = geompy.MakeCompound([Ligne_1, Ligne_2, Ligne_3, Ligne_4, Ligne_5, Ligne_6, Ligne_7, Ligne_8, Ligne_9, Ligne_10, Ligne_11, Ligne_12, Ligne_13, Ligne_14, Ligne_15,Ligne_16,Arc_1, Arc_2])
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
geompy.addToStudy( Sommet_5, 'Sommet_5' )
geompy.addToStudy( Sommet_6, 'Sommet_6' )
geompy.addToStudy( Sommet_7, 'Sommet_7' )
geompy.addToStudy( Sommet_8, 'Sommet_8' )
geompy.addToStudy( Sommet_9, 'Sommet_9' )
geompy.addToStudy( Sommet_10, 'Sommet_10' )
geompy.addToStudy( Sommet_11, 'Sommet_11' )
geompy.addToStudy( Sommet_12, 'Sommet_12' )
geompy.addToStudy( Sommet_13, 'Sommet_13' )
geompy.addToStudy( Sommet_14, 'Sommet_14' )
geompy.addToStudy( Sommet_15, 'Sommet_15' )
geompy.addToStudy( Sommet_16, 'Sommet_16' )
geompy.addToStudy( Sommet_17, 'Sommet_17' )
geompy.addToStudy( Sommet_18, 'Sommet_18' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudyInFather( OX, OX_vertex_3, 'OX:vertex_3' )
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
geompy.addToStudy( Ligne_13, 'Ligne_13' )
geompy.addToStudy( Ligne_14, 'Ligne_14' )
geompy.addToStudy( Ligne_15, 'Ligne_15' )
geompy.addToStudy( Ligne_16, 'Ligne_16' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( Chassis, 'Chassis' )

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
