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

sys.path.insert(0,r'../../../Tools')

###
### GEOM component
###

import GEOM
import geompy
import math
import SALOMEDS
from   numpy import *
from poutreDeStructure import *

#-----------------------------------
#
#  Parametre du probleme
#
#-----------------------------------

Lpoteau         = 5500.
LentreCorniere  = 500.
lentreCorniere  = 300. 
Njoint          = 11
Lcatener        = 3000.
NjointCatener   = 10
LcontreFleche   = 1000.
NjointFleche    = 8
    
geompy.init_geom(theStudy)

# Utilisation du module poutreDeStructure present dans le repertoire
# Tools du dépot pour creer des objets poutres
sp1_1 = geompy.MakeVertex(-LentreCorniere/2.,-lentreCorniere/2.,0.)
sp1_2 = geompy.MakeVertex(-LentreCorniere/2.,-lentreCorniere/2.,Lpoteau)
p1    = poutre('corniereLSW',sp1_1,sp1_2)


sp2_1 = geompy.MakeVertex(LentreCorniere/2.,-lentreCorniere/2.,0.)
sp2_2 = geompy.MakeVertex(LentreCorniere/2.,-lentreCorniere/2.,Lpoteau)
p2    = poutre('corniereLSE',sp2_1,sp2_2)

sp3_1 = geompy.MakeVertex(LentreCorniere/2.,lentreCorniere/2.,0.)
sp3_2 = geompy.MakeVertex(LentreCorniere/2.,lentreCorniere/2.,Lpoteau)
p3    = poutre('corniereLNE',sp3_1,sp3_2)

sp4_1 = geompy.MakeVertex(-LentreCorniere/2.,lentreCorniere/2.,0.)
sp4_2 = geompy.MakeVertex(-LentreCorniere/2.,lentreCorniere/2.,Lpoteau)
p4    = poutre('corniereLNW',sp4_1,sp4_2)

# Une fois les poutres definis on peut rajouter des joint
# espace regulierement a partir d un certain point
poutres= [p1,p2,p3,p4]
Sommets= []
Lignes = []
for p in poutres:
  p.addEvenlySpacedJoint(Lpoteau/Njoint,Njoint,Lpoteau/Njoint)
  p.build()

# On recupere un joint deja existant pour recreer une poutre perpendiculaire
sp5_1 = p2.sommet(8)
coord = geompy.PointCoordinates(sp5_1)
sp5_2 = geompy.MakeVertex(coord[0]+Lcatener,coord[1],coord[2])
p5    = poutre('porteCatener1',sp5_1,sp5_2)

sp6_1 = p3.sommet(8)
coord = geompy.PointCoordinates(sp6_1)
sp6_2 = geompy.MakeVertex(coord[0]+Lcatener,coord[1],coord[2])
p6    = poutre('porteCatener2',sp6_1,sp6_2)

for p in [p5,p6]:
  p.addEvenlySpacedJoint(Lcatener/NjointCatener,NjointCatener,Lcatener/Njoint)
  p.build()

# On utilise la macro creerPoutresEntre pour creer des poutres entre
# les joints de deux poutres
tir11 = creerPoutresEntre('tirant11',p1,p2,1,2,5,2) 
tir12 = creerPoutresEntre('tirant12',p2,p1,2,3,5,2) 
tir21 = creerPoutresEntre('tirant21',p2,p3,1,2,5,2) 
tir22 = creerPoutresEntre('tirant22',p3,p2,2,3,5,2) 
tir31 = creerPoutresEntre('tirant31',p3,p4,1,2,5,2) 
tir32 = creerPoutresEntre('tirant32',p4,p3,2,3,5,2) 
tir41 = creerPoutresEntre('tirant41',p4,p1,1,2,5,2) 
tir42 = creerPoutresEntre('tirant42',p1,p4,2,3,5,2) 
tirc1 = creerPoutresEntre('cat1',p5,p6,0,1,10,1)
tirc2 = creerPoutresEntre('cat2',p6,p5,0,1,10,1)
tirants=tir11+tir12+tir21+tir22+tir31+tir32+tir41+tir42+tirc1+tirc2

for t in tirants:
  t.build()
poutres+=tirants
poutres+=[p5,p6]

for p in poutres:
  Sp,Lp=p.entities()
  Sommets += Sp
  Lignes  += Lp
#p1.addEvenlySpacedJoint(100.,10,50.)
#p1.addJoint(0.05)
#p1.build()




O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

for i,somm in enumerate(Sommets):
  geompy.addToStudy( Sommets[i], 'Sommet_'+str(i+1) )

for i,ligne in enumerate(Lignes):
    geompy.addToStudy(Lignes[i],'Ligne_'+str(i+1))

# On definit des assemblages a partir des lignes 
# pour affecter chacune des caracteristiques elementaires
# aux poutres
PoutreSW=geompy.MakeCompound(p1.entities()[1])
PoutreSE=geompy.MakeCompound(p2.entities()[1])
PoutreNE=geompy.MakeCompound(p3.entities()[1])
PoutreNW=geompy.MakeCompound(p4.entities()[1])

tirs=[]
for t in tir11+tir12+tir21+tir22+tir31+tir32+tir41+tir42:
  tirs+=t.entities()[1]
TirantFleche=geompy.MakeCompound(tirs)

geompy.addToStudy(PoutreSW,'PoutreSW')
geompy.addToStudy(PoutreSE,'PoutreSE')
geompy.addToStudy(PoutreNE,'PoutreNE')
geompy.addToStudy(PoutreNW,'PoutreNW')
geompy.addToStudy(TirantFleche,'TirantFleche') 

PoutreCatener=geompy.MakeCompound(p5.entities()[1]+p6.entities()[1])
tc=[]
for t in tirc1+tirc2:
  tc+=t.entities()[1]
TirantCatener=geompy.MakeCompound(tc)
geompy.addToStudy(PoutreCatener,'PoutreCatener')
geompy.addToStudy(TirantCatener,'TirantCatener')

# On met tout dans un assemblage Tout pour faciliter le maillage
TOUT=geompy.MakeCompound([PoutreSW,PoutreSE,PoutreNE,PoutreNW,TirantFleche,PoutreCatener,TirantCatener])
geompy.addToStudy(TOUT,'Tout')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
