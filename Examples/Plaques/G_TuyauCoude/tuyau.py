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
sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/Plaques/G_TuyauCoude')

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

sk = geompy.Sketcher3D()
sk.addPointsAbsolute(0, 0, 0)
sk.addPointsAbsolute(0, 3600, 0)
sk.addPointsAbsolute(3600, 3600, 0)
Esquisse_3D_1 = sk.wire()
Cong__1D_1 = geompy.MakeFillet1D(Esquisse_3D_1, 600, [4])
Sommet_1 = geompy.MakeVertex(180, 0, 0)
Sommet_2 = geompy.MakeVertex(-180, 0, 0)
Sommet_3 = geompy.MakeVertex(0, 0, 180)
Cong__1D_1_vertex_3 = geompy.GetSubShape(Cong__1D_1, [3])
Arc_1 = geompy.MakeArcCenter(Cong__1D_1_vertex_3, Sommet_1, Sommet_3,False)
Arc_1_vertex_3 = geompy.GetSubShape(Arc_1, [3])
Arc_2 = geompy.MakeArcCenter(Cong__1D_1_vertex_3, Arc_1_vertex_3, Sommet_2,False)
Contour_1 = geompy.MakeWire([Arc_1, Arc_2], 1e-07)
[geomObj_1,geomObj_2] = geompy.SubShapeAll(Contour_1, geompy.ShapeType["EDGE"])
[geomObj_3,geomObj_4] = geompy.SubShapeAll(Contour_1, geompy.ShapeType["EDGE"])
Tuyau_1 = geompy.MakePipe(Contour_1, Cong__1D_1)
listSubShapeIDs = geompy.SubShapeAllIDs(Tuyau_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Tuyau_1, geompy.ShapeType["EDGE"])
listSameIDs = geompy.GetSameIDs(Tuyau_1, geomObj_1)
listSameIDs = geompy.GetSameIDs(Tuyau_1, geomObj_2)
Encastre = geompy.CreateGroup(Tuyau_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Encastre, [7, 14])
listSameIDs = geompy.GetSameIDs(Tuyau_1, geomObj_3)
listSameIDs = geompy.GetSameIDs(Tuyau_1, geomObj_4)
Sym = geompy.CreateGroup(Tuyau_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Sym, [4, 21, 33, 40, 28, 16])
Effort = geompy.CreateGroup(Tuyau_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Effort, [37, 42])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Esquisse_3D_1, 'Esquisse 3D_1' )
geompy.addToStudy( Cong__1D_1, 'Congé 1D_1' )
geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudyInFather( Cong__1D_1, Cong__1D_1_vertex_3, 'Congé 1D_1:vertex_3' )
geompy.addToStudyInFather( Arc_1, Arc_1_vertex_3, 'Arc_1:vertex_3' )
geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( Contour_1, 'Contour_1' )
geompy.addToStudy( Tuyau_1, 'Tuyau_1' )

geompy.addToStudyInFather( Tuyau_1, Encastre, 'Encastre' )
geompy.addToStudyInFather( Tuyau_1, Sym, 'Sym' )
geompy.addToStudyInFather( Tuyau_1, Effort, 'Effort' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
