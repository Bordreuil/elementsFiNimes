# -*- coding: iso-8859-1 -*-

###
### This file is generated automatically by SALOME v6.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
#theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.notebook

###
### GEOM component
###

import GEOM
import math
import SALOMEDS


from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

from numpy import *
distanceEntreJoint = 2000.
hauteurTreillis    = 1500.
largeurTreillis    = 1500.
hauteurAncrageCable = 7500.
nbreDeJoint        = 40
Sommets            = []
Lignes             = []
for i in arange(0,nbreDeJoint+1,1):
  Sommets.append(geompy.MakeVertex(float(i*distanceEntreJoint),0.,0.))
for i in arange(nbreDeJoint-1):
   Sommets.append(geompy.MakeVertex(float((i+1)*distanceEntreJoint),largeurTreillis/2.,hauteurTreillis))
for i in arange(0,nbreDeJoint+1,1):
   Sommets.append(geompy.MakeVertex(float(i*distanceEntreJoint),largeurTreillis,0))

Sommets.append(geompy.MakeVertex(0.,0.,hauteurAncrageCable))



for i in arange(0,nbreDeJoint,1):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i],Sommets[i+1]))
for i in arange(0,nbreDeJoint-2,1):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i+nbreDeJoint+1],Sommets[i+1+nbreDeJoint+1]))
for i in arange(0,nbreDeJoint,1):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i+2*nbreDeJoint],Sommets[i+1+2*nbreDeJoint]))
for i in arange(0,nbreDeJoint+1,2):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i],Sommets[i+2*nbreDeJoint]))
for i in arange(0,nbreDeJoint,2):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i],Sommets[i+nbreDeJoint+1]))
for i in arange(0,nbreDeJoint,2):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i+2*nbreDeJoint],Sommets[i+nbreDeJoint+1]))
for i in arange(0,nbreDeJoint,2):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i+nbreDeJoint+1],Sommets[i+2]))
for i in arange(0,nbreDeJoint,2):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[i+nbreDeJoint+1],Sommets[i+2+2*nbreDeJoint]))
Lignes.append(geompy.MakeLineTwoPnt(Sommets[2*nbreDeJoint-1],Sommets[-1]))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
for i,som in enumerate(Sommets):
  geompy.addToStudy( som, 'Sommet_'+str(i+1) )
for i,lig in enumerate(Lignes):
  geompy.addToStudy(lig,'Ligne_'+str(i))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
