#   On analyse le comportement d un anneau (maillon) de levage pour 
#   determiner la distribution des contraintes
#
#  
#    

# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.5.0 with dump python functionality
###
#Chemin ou se trouve l analyse
currentPath=r'/home/bordreuil/Enseignement/elementsFiNimes/AB_Anneau'
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

#----Initialisation du module geometrie
geompy.init_geom(theStudy)

# Caracteristiques geometriques de l'anneau
rayon           = 25.
longu           = 50.

Sommet_1        = geompy.MakeVertex(0, rayon+longu, 0)
[geomObj_1]     = geompy.SubShapeAll(Sommet_1, geompy.ShapeType["VERTEX"])
[geomObj_2]     = geompy.SubShapeAll(Sommet_1, geompy.ShapeType["VERTEX"])
Sommet_2        = geompy.MakeVertex(rayon, longu, 0)
Sommet_3        = geompy.MakeVertex(rayon, 0, 0)
[geomObj_3]     = geompy.SubShapeAll(Sommet_3, geompy.ShapeType["VERTEX"])
[geomObj_4]     = geompy.SubShapeAll(Sommet_3, geompy.ShapeType["VERTEX"])
Sommet_4        = geompy.MakeVertex(0, longu, 0)

Arc_1           = geompy.MakeArcCenter(Sommet_4, Sommet_1, Sommet_2,False)
Ligne_1         = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Anneau          = geompy.MakeWire([Arc_1, Ligne_1], 1e-07)

# definition du point haut pour encastrement
listSubShapeIDs = geompy.SubShapeAllIDs(Anneau, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Anneau, geompy.ShapeType["VERTEX"])
listSameIDs     = geompy.GetSameIDs(Anneau, geomObj_1)
Haut            = geompy.CreateGroup(Anneau, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Haut, [3])

# definition du point bas pour application de la force
listSameIDs = geompy.GetSameIDs(Anneau, geomObj_2)
listSameIDs = geompy.GetSameIDs(Anneau, geomObj_3)
Bas         = geompy.CreateGroup(Anneau, geompy.ShapeType["VERTEX"])
geompy.UnionIDs(Bas, [6])
listSameIDs = geompy.GetSameIDs(Anneau, geomObj_4)

geompy.addToStudy( Sommet_1, 'Sommet_1' )
geompy.addToStudy( Sommet_2, 'Sommet_2' )
geompy.addToStudy( Sommet_3, 'Sommet_3' )
geompy.addToStudy( Sommet_4, 'Sommet_4' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )
geompy.addToStudy(Anneau, 'Anneau' )
geompy.addToStudyInFather( Anneau, Haut, 'Haut' )
geompy.addToStudyInFather( Anneau, Bas, 'Bas' )

### Store presentation parameters of displayed objects
import iparameters
ipar = iparameters.IParameters(theStudy.GetModuleParameters("Interface Applicative", "GEOM", 1))

#Set up entries:
# set up entry GEOM_1 (Sommet_1) parameters


import smesh, SMESH, SALOMEDS
# Definition du maillage
smesh.SetCurrentStudy(theStudy)
import StdMeshers
Maillage_1    = smesh.Mesh(Anneau)
Regular_1D    = Maillage_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(15,[],[  ])
Nb_Segments_1.SetDistrType( 0 )
isDone        = Maillage_1.Compute()
TOUT          = Maillage_1.GroupOnGeom(Anneau,'Anneau',SMESH.EDGE)
Bas_1         = Maillage_1.GroupOnGeom(Bas,'Bas',SMESH.NODE)
Haut_1        = Maillage_1.GroupOnGeom(Haut,'Haut',SMESH.NODE)
TOUT.SetName( 'TOUT' )
[ TOUT, Bas_1, Haut_1 ] = Maillage_1.GetGroups()
smesh.SetName(Maillage_1, 'Maillage_1')
Maillage_1.ExportMED( currentPath, 0, SMESH.MED_V2_2, 1 )

## set object names
smesh.SetName(Maillage_1.GetMesh(), 'Maillage_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Nb_Segments_1, 'Nb. Segments_1')
smesh.SetName(TOUT, 'TOUT')
smesh.SetName(Bas_1, 'Bas')
smesh.SetName(Haut_1, 'Haut')





if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
  iparameters.getSession().restoreVisualState(1)
