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
Corps        = geompy.MakeCompound([Virole,FondG,FondD])

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

Piq1          = creerPiquageVirole(Position,H,Alpha,Dp,Dbride)
Virole,Piq1   = couperVirolePiquagePos(Piq1,Corps)

Corps  = geompy.MakeCompound([Virole,FondG,FondD])

H        = 1000.
Dp       = 300.
Alpha    = -45.
Position = -800.
Dbride   = 400.

Piq2          = creerPiquageVirole(Position,H,Alpha,Dp,Dbride)
Virole,Piq2   = couperVirolePiquageNeg(Piq2,Corps)

Corps  = geompy.MakeCompound([Virole,FondG,FondD])

Hauteur_P2 = 2500.
R_piquage  = 600.
Alpha      = 45.
Dpiquage2  = 300.
Dpbride2   = 400.

Piq3          = creerPiquageFondAxialPos(Hauteur_P2,R_piquage,Alpha,Dpiquage2,Dpbride2)
FondD,Piq3    = couperFondPiquagePosCas2(Piq3,Corps)
Corps         = geompy.MakeCompound([Virole,FondG,FondD])
Alpha         = 135.
R_piquage     = 300.
Piq4          = creerPiquageFondAxialPos(Hauteur_P2,R_piquage,Alpha,Dpiquage2,Dpbride2)
FondD,Piq4    = couperFondPiquagePosCas3Ou4(Piq4,Corps)

Corps  = geompy.MakeCompound([Virole,FondG,FondD])
Hauteur_P2 = 2400.
R_piquage  = 600.
Alpha      = 0.
Dpiquage2  = 250.
Dpbride2   = 300.

Piq5         = creerPiquageFondAxialPos(Hauteur_P2,R_piquage,Alpha,Dpiquage2,Dpbride2)
FondD,Piq5    = couperFondPiquagePosCas1(Piq5,Corps)
Corps         = geompy.MakeCompound([Virole,FondG,FondD])

Hauteur_P2 = 2750.
R_piquage  = 00.
Alpha      = 0.
Dpiquage2  = 100.
Dpbride2   = 200.

Piq6          = creerPiquageFondAxialPos(Hauteur_P2,R_piquage,Alpha,Dpiquage2,Dpbride2)
FondD,Piq6    = couperFondPiquagePosCas3Ou4(Piq6,Corps)
Corps         = geompy.MakeCompound([Virole,FondG,FondD])

Hauteur_P2 = -2750.
R_piquage  = 600.
Alpha      = 0.
Dpiquage2  = 300.
Dpbride2   = 400.

Piq7          = creerPiquageFondAxialNeg(Hauteur_P2,R_piquage,Alpha,Dpiquage2,Dpbride2)
FondG,Piq7    = couperFondPiquageNegCas1Ou2(Piq7,Corps)
Corps         = geompy.MakeCompound([Virole,FondG,FondD])

Bidon,groupes = creerBidon([FondG,FondD,Virole,Pieds,Piq1,Piq2,Piq3,Piq4,Piq5,Piq6,Piq7])
#-----------------------------------
#  Création du bidon
#-----------------------------------

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

# geompy.addToStudy( Virole, 'Virole' )
# geompy.addToStudy( FondG,'FondG')
# geompy.addToStudy( FondD,'FondD')
# geompy.addToStudy( Pieds, 'Pieds' )
# geompy.addToStudy( Piq1, 'Piquage1' )
# geompy.addToStudy( Piq2, 'Piquage2' )
# geompy.addToStudy( Piq3, 'Piquage3')
# geompy.addToStudy( Piq4, 'Piquage4')
# geompy.addToStudy( Piq5, 'Piquage5')
# geompy.addToStudy( Piq6, 'Piquage6')
# geompy.addToStudy( Piq7, 'Piquage7')
# geompy.addToStudy( Corps, 'Corps')
geompy.addToStudy( Bidon, 'Bidon' )

nameGroups=['FondG','FondD',
            'Virole','Pieds',
            'Piquage1','Piquage2',
            'Piquage3','Piquage4',
            'Piquage5','Piquage6',
            'Piquage7']

for i,group in enumerate(groupes):
   geompy.addToStudyInFather( Bidon,group,nameGroups[i])


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
