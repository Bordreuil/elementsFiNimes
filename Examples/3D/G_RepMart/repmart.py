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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/3D/G_RepMart')

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
Corps_principal = geompy.ImportSTEP("/home/bordreuil/Enseignement/elementsFiNimes/Examples/3D/G_RepMart/piedRepMart.stp")
[Esquisse_1] = geompy.SubShapes(Corps_principal, [56])
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
geomObj_2 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
Corps_principal_1 = geompy.GetSubShape(Corps_principal, [261])
Esquisse_1 = geompy.MakeSketcherOnPlane("Sketcher:F -0.050000 0.000000:TT 0.050000 0.000000:TT 0.050000 -0.050000:TT -0.050000 -0.050000:WW", Corps_principal_1 )
Enl_vement_extrud__1 = geompy.MakeExtrudedCut(Corps_principal, Esquisse_1, 90, 0)
[Appui1] = geompy.SubShapes(Enl_vement_extrud__1, [278])
[Appui2] = geompy.SubShapes(Enl_vement_extrud__1, [309])
[Tige] = geompy.SubShapes(Enl_vement_extrud__1, [349])

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Corps_principal, 'Corps principal' )
geompy.addToStudy( Esquisse_1, 'Esquisse_1' )
geompy.addToStudyInFather( Corps_principal, Corps_principal_1, 'Corps principal' )
geompy.addToStudy( Enl_vement_extrud__1, 'Enlèvement_extrudé_1' )
geompy.addToStudyInFather( Enl_vement_extrud__1, Appui1, 'Appui1' )
geompy.addToStudyInFather( Enl_vement_extrud__1, Appui2, 'Appui2' )
geompy.addToStudyInFather( Enl_vement_extrud__1, Tige, 'Tige' )



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
