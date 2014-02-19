# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.5.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook
#sys.path.insert( 0, r'/home/bordreuil/Enseignement/elementsFiNimes/Examples/C_BMXPoutre')

import iparameters
ipar = iparameters.IParameters(salome.myStudy.GetCommonParameters("Interface Applicative", 1), True)

ipar.append("AP_MODULES_LIST", "Geometry")
ipar.append("AP_MODULES_LIST", "Mesh")


###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS


geompy.init_geom(theStudy)
x_0 = 0.;   y_0 = 0.;
x_1 = 5.;   y_1 = -100.;
x_2 = -500.;y_2 = -10.;
x_3 = -475.;y_3 = -400.;
x_4 = -550.;y_4 = -425.; z_4 = 50.;
x_5 = -530.;y_5 = -50.;  z_5 = 40.;
x_6 = -900.;y_6 = -480.; z_6 = 85.;
x_7 = 75. ;y_7 = -450 ;z_7=0.;

# Definition des points
Sommet_1   = geompy.MakeVertex(x_0 ,y_0 , 0.)
Sommet_2   = geompy.MakeVertex(x_1 ,y_1 , 0.)
Sommet_3   = geompy.MakeVertex(x_2 ,y_2 , 0.)
Sommet_4   = geompy.MakeVertex(x_3 ,y_3 , 0.)
Sommet_5   = geompy.MakeVertex(x_4 ,y_4 , z_4)
Sommet_6   = geompy.MakeVertex(x_4 ,y_4 , -z_4)
Sommet_7   = geompy.MakeVertex(x_5 ,y_5 , z_5)
Sommet_8   = geompy.MakeVertex(x_5 ,y_5 , -z_5)
Sommet_9   = geompy.MakeVertex(x_6 ,y_6 , z_6)
Sommet_10  = geompy.MakeVertex(x_6 ,y_6 ,-z_6)
Sommet_11  = geompy.MakeVertex(x_7 ,y_7 , z_7)


Direction = geompy.MakeLineTwoPnt(Sommet_1, Sommet_2)
Barre_sup = geompy.MakeLineTwoPnt(Sommet_1, Sommet_3)
Barre_inf = geompy.MakeLineTwoPnt(Sommet_2, Sommet_4)
Barre_selle = geompy.MakeLineTwoPnt(Sommet_3, Sommet_4)
Arriere_bas_1 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_5)
Arriere_bas_2 = geompy.MakeLineTwoPnt(Sommet_4, Sommet_6)
Arriere_bas_3 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_10)
Arriere_bas_4 = geompy.MakeLineTwoPnt(Sommet_5, Sommet_9)
Arriere_haut_1 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_7)
Arriere_haut_2 = geompy.MakeLineTwoPnt(Sommet_3, Sommet_8)
Arriere_haut_3 = geompy.MakeLineTwoPnt(Sommet_8, Sommet_10)
Arriere_haut_4 = geompy.MakeLineTwoPnt(Sommet_7, Sommet_9)
Fourche = geompy.MakeLineTwoPnt(Sommet_2, Sommet_11)
Cadre = geompy.MakeCompound([Direction, Barre_sup, Barre_inf, Barre_selle, Fourche, Arriere_bas_1, Arriere_bas_2, Arriere_bas_3, Arriere_bas_4, Arriere_haut_1, Arriere_haut_2, Arriere_haut_3, Arriere_haut_4])
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
geompy.addToStudy( Direction, 'Direction' )
geompy.addToStudy( Barre_sup, 'Barre_sup' )
geompy.addToStudy( Barre_inf, 'Barre_inf' )
geompy.addToStudy( Barre_selle, 'Barre_selle' )
geompy.addToStudy( Arriere_bas_1, 'Arriere_bas_1' )
geompy.addToStudy( Arriere_bas_2, 'Arriere_bas_2' )
geompy.addToStudy( Arriere_bas_3, 'Arriere_bas_3' )
geompy.addToStudy( Arriere_bas_4, 'Arriere_bas_4' )
geompy.addToStudy( Arriere_haut_1, 'Arriere_haut_1' )
geompy.addToStudy( Arriere_haut_2, 'Arriere_haut_2' )
geompy.addToStudy( Arriere_haut_3, 'Arriere_haut_3' )
geompy.addToStudy( Arriere_haut_4, 'Arriere_haut_4' )
geompy.addToStudy( Fourche, 'Fourche' )
geompy.addToStudy( Cadre, 'Cadre' )

##


###
### SMESH component
###

import smesh, SMESH, SALOMEDS

smesh.SetCurrentStudy(theStudy)
import StdMeshers
Nb_Segments_1 = smesh.CreateHypothesis('NumberOfSegments')
Nb_Segments_1.SetNumberOfSegments( 10 )
Nb_Segments_1.SetDistrType( 0 )

Regular_1D = smesh.CreateHypothesis('Regular_1D')

Maillage_1 = smesh.Mesh(Cadre)
status = Maillage_1.AddHypothesis(Nb_Segments_1)
status = Maillage_1.AddHypothesis(Regular_1D)
isDone = Maillage_1.Compute()
TOUT = Maillage_1.CreateEmptyGroup( SMESH.EDGE, 'TOUT' )
nbAdd = TOUT.Add( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130 ] )
TOUT.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
Fourche_1 = Maillage_1.CreateEmptyGroup( SMESH.EDGE, 'Fourche' )
nbAdd = Fourche_1.Add( [ 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 ] )
Fourche_1.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
Direct = Maillage_1.CreateEmptyGroup( SMESH.EDGE, 'Direct' )
nbAdd = Direct.Add( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] )
Direct.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
Arr = Maillage_1.CreateEmptyGroup( SMESH.EDGE, 'Arr' )
nbAdd = Arr.Add( [ 52, 53, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130 ] )
Arr.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
AxeAv = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'AxeAv' )
nbAdd = AxeAv.Add( [ 5 ] )
AxeAv.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
AxeAr = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'AxeAr' )
nbAdd = AxeAr.Add( [ 9, 8 ] )
AxeAr.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
Pedale = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Pedale' )
nbAdd = Pedale.Add( [ 4 ] )
Pedale.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
Potence = Maillage_1.CreateEmptyGroup( SMESH.NODE, 'Potence' )
nbAdd = Potence.Add( [ 1 ] )
Potence.SetColor( SALOMEDS.Color( 0, 0.666667, 1 ))
isDone = Maillage_1.Compute()


smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(Regular_1D, 'Regular_1D')
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(TOUT, 'TOUT')
smesh.SetName(Fourche_1, 'Fourche')
smesh.SetName(Direct, 'Direct')
smesh.SetName(Arr, 'Arr')
smesh.SetName(AxeAv, 'AxeAv')
smesh.SetName(AxeAr, 'AxeAr')
smesh.SetName(Pedale, 'Pedale')
smesh.SetName(Potence, 'Potence')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
  iparameters.getSession().restoreVisualState(1)
