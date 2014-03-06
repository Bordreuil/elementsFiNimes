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


Lx   = 250. # Demi-Longueur de la virole
Rb   = 250. # Rayon du bidon
Rp   = 40.  # Rayon du piquage
Rbri = 60.  # Rayon de bride au niveau du piquage
Lp   = 300.

Xber = 200. # Position des berceaux
Lber = 250. # Longueur des berceaux
dBer = 50.  # hauteur du berceau 

geompy.init_geom(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

Sommet_1 = geompy.MakeVertex(-Lx, 0, 0)
Sommet_2 = geompy.MakeVertex(-Lx, Rb, 0)
Sommet_3 = geompy.MakeVertex(Lx, Rb, 0)
Sommet_4 = geompy.MakeVertex(Lx, 0, 0)

Sommet_5 = geompy.MakeVertex(0, 0, 0)
Sommet_6 = geompy.MakeVertex(0, Lp, 0)

Sommet_7  = geompy.MakeVertex(Lx+Rb, 0, 0)
Sommet_8  = geompy.MakeVertex(-(Lx+Rb), 0, 0)

Sommet_9  = geompy.MakeVertex(-Xber, -Rb+dBer, -Lber/2.)
Sommet_10 = geompy.MakeVertex(-Xber, -Rb+dBer, Lber/2.)
Sommet_11 = geompy.MakeVertex(-Xber, -Rb-dBer, Lber/2.)
Sommet_12 = geompy.MakeVertex(-Xber, -Rb-dBer, -Lber/2.)

Sommet_13  = geompy.MakeVertex(Xber, -Rb+dBer, -Lber/2.)
Sommet_14 = geompy.MakeVertex(Xber, -Rb+dBer, Lber/2.)
Sommet_15 = geompy.MakeVertex(Xber, -Rb-dBer, Lber/2.)
Sommet_16 = geompy.MakeVertex(Xber, -Rb-dBer, -Lber/2.)

# Creation de la forme de revolution
Ligne_1 = geompy.MakeLineTwoPnt(Sommet_2, Sommet_3)
Arc_1 = geompy.MakeArcCenter(Sommet_1, Sommet_8, Sommet_2,False)
Arc_2 = geompy.MakeArcCenter(Sommet_4, Sommet_3, Sommet_7,False)
profil = geompy.MakeWire([Ligne_1, Arc_1, Arc_2], 1e-07)
R_volution_1 = geompy.MakeRevolution(profil, OX, 360*math.pi/180.0)

# Creation de la geometrie du piquage
Ligne_2 = geompy.MakeLineTwoPnt(Sommet_6, Sommet_5)
Cercle_1 = geompy.MakeCircle(Sommet_6, Ligne_2, Rp)
Extrusion_1 = geompy.MakePrismVecH(Cercle_1, Ligne_2, 100)
Cercle_2 = geompy.MakeCircle(Sommet_6, Ligne_2, Rbri)


Ligne_3 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_10)
Ligne_4 = geompy.MakeLineTwoPnt(Sommet_10, Sommet_11)
Ligne_5 = geompy.MakeLineTwoPnt(Sommet_11, Sommet_12)
Ligne_6 = geompy.MakeLineTwoPnt(Sommet_9, Sommet_12)

Ligne_7 = geompy.MakeLineTwoPnt(Sommet_13, Sommet_14)
Ligne_8 = geompy.MakeLineTwoPnt(Sommet_14, Sommet_15)
Ligne_9 = geompy.MakeLineTwoPnt(Sommet_15, Sommet_16)
Ligne_10 = geompy.MakeLineTwoPnt(Sommet_16, Sommet_13)

Face_1 = geompy.MakeFaceWires([Cercle_1, Cercle_2], 1)
Face_15 = geompy.MakeFaceWires([Ligne_3, Ligne_4, Ligne_5, Ligne_6], 1)
Face_16 = geompy.MakeFaceWires([Ligne_7, Ligne_8, Ligne_9, Ligne_10], 1)

Partition_1 = geompy.MakePartition([Extrusion_1], [R_volution_1], [], [], geompy.ShapeType["FACE"], 0, [], 0)
[Partition_2,Face_3] = geompy.ExtractShapes(Partition_1, geompy.ShapeType["FACE"], True)
Partition_2 = geompy.MakePartition([R_volution_1], [Extrusion_1], [], [], geompy.ShapeType["FACE"], 0, [], 0)
[Face_2,Face_4,Partition_3,Face_5,Face_7] = geompy.ExtractShapes(Partition_2, geompy.ShapeType["FACE"], True)
Partition_3 = geompy.MakePartition([Face_15, Face_16], [Partition_2], [], [], geompy.ShapeType["FACE"], 0, [], 0)
[Face_5,Virole,Face_8,Fonds] = geompy.ExtractShapes(Partition_3, geompy.ShapeType["FACE"], True)
Virole = geompy.MakeCompound([Face_4])
Fonds = geompy.MakeCompound([Face_2, Face_7])
Piquage = geompy.MakeCompound([Face_1, Face_3])
Supports = geompy.MakeCompound([Face_5, Face_8])
ViroleS = geompy.MakeFuse(Virole, Supports)
Bidon = geompy.MakeCompound([Fonds, Piquage, ViroleS])
Encastre = geompy.CreateGroup(Bidon, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Encastre, [59])
Appui = geompy.CreateGroup(Bidon, geompy.ShapeType["EDGE"])
geompy.UnionIDs(Appui, [66])
Fonds_1 = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
geompy.UnionIDs(Fonds_1, [3, 10])
Virole_1 = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
geompy.UnionIDs(Virole_1, [37])
Bride_1 = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
geompy.UnionIDs(Bride_1, [18])
Piquage_2 = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
geompy.UnionIDs(Piquage_2, [25])

Supports_1 = geompy.CreateGroup(Bidon, geompy.ShapeType["FACE"])
geompy.UnionIDs(Supports_1, [55, 62])


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
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Ligne_1, 'Ligne_1' )

geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( profil, 'profil' )
geompy.addToStudy( R_volution_1, 'Révolution_1' )


geompy.addToStudy( Ligne_2, 'Ligne_2' )
geompy.addToStudy( Cercle_1, 'Cercle_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Cercle_2, 'Cercle_2' )
geompy.addToStudy( Ligne_3, 'Ligne_3' )
geompy.addToStudy( Ligne_4, 'Ligne_4' )
geompy.addToStudy( Ligne_5, 'Ligne_5' )
geompy.addToStudy( Ligne_6, 'Ligne_6' )
geompy.addToStudy( Ligne_7, 'Ligne_7' )
geompy.addToStudy( Ligne_8, 'Ligne_8' )
geompy.addToStudy( Ligne_9, 'Ligne_9' )
geompy.addToStudy( Ligne_10, 'Ligne_10' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_15, 'Face_15' )
geompy.addToStudy( Face_16, 'Face_16' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( Partition_2, 'Partition_2' )
geompy.addToStudyInFather( Partition_1, Face_3, 'Face_3' )
geompy.addToStudyInFather( Partition_2, Face_2, 'Face_2' )
geompy.addToStudyInFather( Partition_2, Face_4, 'Face_4' )
geompy.addToStudyInFather( Partition_2, Face_7, 'Face_7' )
geompy.addToStudy( Partition_3, 'Partition_3' )
geompy.addToStudyInFather( Partition_3, Face_5, 'Face_5' )

geompy.addToStudy( Virole, 'Virole' )
geompy.addToStudyInFather( Partition_3, Face_8, 'Face_8' )
geompy.addToStudy( Fonds, 'Fonds' )
geompy.addToStudy( Piquage, 'Piquage' )
geompy.addToStudy( Supports, 'Supports' )
geompy.addToStudy( ViroleS, 'ViroleS' )
geompy.addToStudy( Bidon, 'Bidon' )
geompy.addToStudyInFather( Bidon, Encastre, 'Encastre' )
geompy.addToStudyInFather( Bidon, Appui, 'Appui' )
geompy.addToStudyInFather( Bidon, Fonds_1, 'Fonds' )
geompy.addToStudyInFather( Bidon, Virole_1, 'Virole' )
geompy.addToStudyInFather( Bidon, Bride_1, 'Bride' )
geompy.addToStudyInFather( Bidon, Piquage_2, 'Piquage' )
geompy.addToStudyInFather( Bidon, Supports_1, 'Supports' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
