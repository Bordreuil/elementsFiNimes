# -*- coding: iso-8859-1 -*-
#
#   Projet Parant - Happiette 
#   Creation d un module d appareil sous pression
###


import sys
import salome
import sys
sys.path.append('/home/bordreuil/Enseignement/elementsFiNimes/Tools')
salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook
sys.path.insert( 0, r'/home/polytux/elementsFinis/ProjetMeca')

###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS
from   numpy import *
from   bidonChar import *

geompy.init_geom(theStudy)
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

#-----------------------------------
#  Création du bidon
#-----------------------------------
#-----------------------------------
#  Parametres du bidon
#-----------------------------------
D = 1600.
L = 4000.

Virole,FondG,FondD = creerViroleEtDeuxGRC(L,D,OX)

#-----------------------------------
#  Création des pieds
#-----------------------------------
#-----------------------------------
#  Parametres des pieds
#-----------------------------------
Position_pieds = 1280.
Largeur_pieds  = 900.
largeur_pieds  = 300.
Hauteur_pieds  = 800.


Pied1,Pied2 = creerPiedsEnU(Position_pieds,largeur_pieds,Largeur_pieds,Hauteur_pieds,D)

Corps  = geompy.MakeCompound([Virole,FondG,FondD])

Virole,Pieds = couperPiedEtBidon(Pied1,Pied2,Corps)
Corps  = geompy.MakeCompound([Virole,FondG,FondD])

#-----------------------------------
#  Creation du piquage
#-----------------------------------
#-----------------------------------
#  Parametres du piquage
# A faire : 0<Dp<D      -180<Alpha<180      H>D/2     Dbride>Dp    Position <(L/2)-(Dp/2)
#-----------------------------------
H        = 1000.
Dp       = 500.
Alpha    = 90.
Position = 1300.
Dbride   = 600.

Piq1          = creerPiquage(Position,H,Alpha,Dp,Dbride)
Virole,Piq1   = couperVirolePiquage(Piq1,Corps)

Corps  = geompy.MakeCompound([Virole,FondG,FondD])

H        = 1000.
Dp       = 300.
Alpha    = -45.
Position = 800.
Dbride   = 400.

Piq2          = creerPiquage(Position,H,Alpha,Dp,Dbride)
Virole,Piq2   = couperVirolePiquage(Piq2,Corps)

Bidon,groupes = creerBidon([FondG,FondD,Virole,Pieds,Piq1,Piq2])
#-----------------------------------
#  Création du bidon
#-----------------------------------

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

geompy.addToStudy( Virole, 'Virole' )
geompy.addToStudy( FondG,'FondG')
geompy.addToStudy( FondD,'FondD')
geompy.addToStudy( Pieds, 'Pieds' )
geompy.addToStudy( Piq1, 'Piquage1' )
geompy.addToStudy( Piq2, 'Piquage2' )
geompy.addToStudy( Bidon, 'Bidon' )
nameGroups=['FondG','FondD','Virole','Pieds','Piquage1','Piquage2']
for i,group in enumerate(groupes):
  geompy.addToStudyInFather( Bidon,group,nameGroups[i])


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
