# -*- coding: iso-8859-1 -*-
#
#   Projet Parant - Happiette 
#   Creation d un module d appareil sous pression
###


import sys
import salome
import sys
# On doit s
sys.path.append('../../Tools')
salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook
#sys.path.insert( 0, r'/home/polytux/elementsFinis/ProjetMeca')

###
### GEOM component
###

import GEOM

from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

import math
import SALOMEDS
from   numpy import *
from   bidonPar import *

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
Position_pieds = 1280.
Largeur_pieds  = 900.
largeur_pieds  = 300.
Hauteur_pieds  = 800.
bfg = bidonFondGRC(D,L,Position_pieds,Largeur_pieds,largeur_pieds,Hauteur_pieds,geomPy=geompy)

#-----------------------------------
#  Parametres du piquage
# A faire : 0<Dp<D      -180<Alpha<180      H>D/2     Dbride>Dp    Position <(L/2)-(Dp/2)
#-----------------------------------
H        = 1000.
Dp       = 500.
Alpha    = 90.
Position = 1300.
Dbride   = 600.

bfg.ajouterPiquageVirole('Piquage1',H,Dp,Alpha,Position,Dbride)
bfg.ajouterPiquageVirole('Piquage2',H,Dp,45,-Position,Dbride)
bfg.ajouterPiquageAxialFond('Piquage3','Gauche',-2500.,300,45,600.,400.)
bfg.ajouterPiquageAxialFond('Piquage4','Droite',2500.,300 ,45,400.,400.)

Bidon,groupes = bfg.fabriquerBidon()
#-----------------------------------
#  Création du bidon
#-----------------------------------

# geompy.addToStudy( O, 'O' )
# geompy.addToStudy( OX, 'OX' )
# geompy.addToStudy( OY, 'OY' )
# geompy.addToStudy( OZ, 'OZ' )


geompy.addToStudy( Bidon, 'Bidon' )
nameGroups = bfg.groups()

for i,group in enumerate(groupes):
  geompy.addToStudyInFather( Bidon,group,nameGroups[i])


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

bfg.genererPointComm()
