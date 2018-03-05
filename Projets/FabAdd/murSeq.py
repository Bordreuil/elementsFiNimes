# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/bordreuil/Enseignement/Polytech/Projets/2018/Ther3DFabAdd')

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
Lcordon = 3.
LZat    = 10.
LSub    = 30.
ESub    = 20.
Passe   = [1,2]# ou [2,3]
poSects= [-10.,0.,20.,25.,90.,100.]
Sommets=[]
for sect in poSects: 
  Sommets.append(geompy.MakeVertex(0, sect, 0))              #  Sommet_1 
  Sommets.append(geompy.MakeVertex(Lcordon, sect, 0))        # Sommet_2 
  Sommets.append(geompy.MakeVertex(LZat, sect, 0))           # Sommet_3 
  Sommets.append(geompy.MakeVertex(LSub, sect, 0))           # Sommet_4 
  Sommets.append(geompy.MakeVertex(0, sect, -Lcordon))       # Sommet_5 
  Sommets.append(geompy.MakeVertex(Lcordon, sect, -Lcordon)) # Sommet_6 
  Sommets.append(geompy.MakeVertex(0, sect, -LZat))          # Sommet_7 
  Sommets.append(geompy.MakeVertex(LZat, sect, -LZat))       # Sommet_8 
  Sommets.append(geompy.MakeVertex(0, sect, -ESub))          # Sommet_9
  Sommets.append(geompy.MakeVertex(LSub, sect, -ESub))       # Sommet_10 
  Sommets.append(geompy.MakeVertex(0, sect,Lcordon))         # Sommet_11 
  Sommets.append(geompy.MakeVertex(Lcordon, sect,Lcordon))   # Sommet_12
nbParSect = 12

Lignes=[]
print '----Construction des lignes des sections'
for i,sect in enumerate(poSects):
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[0+i*nbParSect], Sommets[1+i*nbParSect]))  # Ligne_1 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[1+i*nbParSect], Sommets[2+i*nbParSect]))  # Ligne_2 = 
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[2+i*nbParSect], Sommets[3+i*nbParSect]))  # Ligne_3 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[3+i*nbParSect], Sommets[9+i*nbParSect]))  # Ligne_4 = 
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[9+i*nbParSect], Sommets[8+i*nbParSect]))  # Ligne_5 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[8+i*nbParSect], Sommets[6+i*nbParSect]))  # Ligne_6 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[6+i*nbParSect], Sommets[4+i*nbParSect]))  # Ligne_7 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[4+i*nbParSect], Sommets[0+i*nbParSect]))  # Ligne_8 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[5+i*nbParSect], Sommets[4+i*nbParSect]))  # Ligne_9 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[5+i*nbParSect], Sommets[1+i*nbParSect]))  # Ligne_10 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[5+i*nbParSect], Sommets[7+i*nbParSect]))  # Ligne_11 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[7+i*nbParSect], Sommets[9+i*nbParSect]))  # Ligne_12 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[7+i*nbParSect], Sommets[6+i*nbParSect]))  # Ligne_13 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[7+i*nbParSect], Sommets[2+i*nbParSect]))  # Ligne_14 =
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[0+i*nbParSect], Sommets[10+i*nbParSect])) # Ligne_15 = 
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[10+i*nbParSect], Sommets[11+i*nbParSect]))# Ligne_16 = 
  Lignes.append(geompy.MakeLineTwoPnt(Sommets[1+i*nbParSect], Sommets[11+i*nbParSect])) # Ligne_17 =

print '----Construction des faces des sections'
Faces=[]
numFacesSectDeb=[0]
for i,sect in enumerate(poSects):
  Faces.append(geompy.MakeFaceWires([Lignes[0+i*17], Lignes[7+i*17], Lignes[8+i*17], Lignes[9+i*17]], 1))  # Face_1 = 
  Faces.append(geompy.MakeFaceWires([Lignes[1+i*17], Lignes[9+i*17], Lignes[10+i*17], Lignes[13+i*17]], 1)) # Face_2 = 
  Faces.append(geompy.MakeFaceWires([Lignes[6+i*17], Lignes[8+i*17], Lignes[10+i*17], Lignes[12+i*17]], 1))  # Face_3 = 
  Faces.append(geompy.MakeFaceWires([Lignes[2+i*17], Lignes[3+i*17], Lignes[11+i*17], Lignes[13+i*17]], 1))  # Face_4 = 
  Faces.append(geompy.MakeFaceWires([Lignes[4+i*17], Lignes[5+i*17], Lignes[11+i*17], Lignes[12+i*17]], 1))  # Face_5 = 
  Faces.append(geompy.MakeFaceWires([Lignes[0+i*17], Lignes[16+i*17], Lignes[15+i*17], Lignes[14+i*17]], 1)) # Face_6 =
  numFacesSectDeb.append(len(Faces))

numLigneBase = len(Lignes)
print '----------------Nombre de Lignes de base:',numLigneBase,' nombre de ligne par section:',numLigneBase/len(poSects)
numFaceBase  = len(Faces)
print '----------------Nombre de Faces de base:',numFaceBase,' nombre de face par section:',numFaceBase/len(poSects)
print '----Construction des lignes liant les sections'

for i in range(len(poSects)-1):
  for j in range(nbParSect):
    Lignes.append(geompy.MakeLineTwoPnt(Sommets[j+i*nbParSect],Sommets[j+(i+1)*nbParSect]))
#print 'Nombre de Lignes:',len(Lignes)

numFacesJoint=[len(Faces)]
print '----Construction des faces liant les sections'
for i in range(len(poSects)-1):
   Faces.append(geompy.MakeFaceWires([Lignes[0+i*17], Lignes[17+i*17], Lignes[numLigneBase+i*nbParSect], Lignes[numLigneBase+1+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[1+i*17], Lignes[18+i*17], Lignes[numLigneBase+1+i*nbParSect], Lignes[numLigneBase+2+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[2+i*17], Lignes[19+i*17], Lignes[numLigneBase+2+i*nbParSect], Lignes[numLigneBase+3+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[3+i*17], Lignes[20+i*17], Lignes[numLigneBase+3+i*nbParSect], Lignes[numLigneBase+9+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[4+i*17], Lignes[21+i*17], Lignes[numLigneBase+8+i*nbParSect], Lignes[numLigneBase+9+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[5+i*17], Lignes[22+i*17], Lignes[numLigneBase+6+i*nbParSect], Lignes[numLigneBase+8+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[6+i*17], Lignes[23+i*17], Lignes[numLigneBase+4+i*nbParSect], Lignes[numLigneBase+6+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[7+i*17], Lignes[24+i*17], Lignes[numLigneBase+i*nbParSect], Lignes[numLigneBase+4+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[9+i*17], Lignes[26+i*17], Lignes[numLigneBase+1+i*nbParSect], Lignes[numLigneBase+5+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[10+i*17], Lignes[27+i*17], Lignes[numLigneBase+5+i*nbParSect], Lignes[numLigneBase+7+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[12+i*17], Lignes[29+i*17], Lignes[numLigneBase+6+i*nbParSect], Lignes[numLigneBase+7+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[11+i*17], Lignes[28+i*17], Lignes[numLigneBase+7+i*nbParSect], Lignes[numLigneBase+9+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[13+i*17], Lignes[30+i*17], Lignes[numLigneBase+2+i*nbParSect], Lignes[numLigneBase+7+i*nbParSect]], 1))
   Faces.append(geompy.MakeFaceWires([Lignes[8+i*17] , Lignes[25+i*17], Lignes[numLigneBase+4+i*nbParSect], Lignes[numLigneBase+5+i*nbParSect]], 1))
   if (i in Passe):
        Faces.append(geompy.MakeFaceWires([Lignes[14+i*17] , Lignes[31+i*17], Lignes[numLigneBase+i*nbParSect], Lignes[numLigneBase+10+i*nbParSect]], 1))
        Faces.append(geompy.MakeFaceWires([Lignes[15+i*17] , Lignes[32+i*17], Lignes[numLigneBase+10+i*nbParSect], Lignes[numLigneBase+11+i*nbParSect]], 1))
        Faces.append(geompy.MakeFaceWires([Lignes[16+i*17] , Lignes[33+i*17], Lignes[numLigneBase+1+i*nbParSect], Lignes[numLigneBase+11+i*nbParSect]], 1))

   numFacesJoint.append(len(Faces))
numLigne = len(Lignes)
print '----------------Nombre de Lignes:',numLigne,' nombre de ligne par section:',numLigneBase/len(poSects)
numFace  = len(Faces)
print '----------------Nombre de Faces:',numFace,' nombre de face par section:',numFaceBase/len(poSects)
print numFacesSectDeb,numFacesJoint

Coques=[]
print
for i in range(len(poSects)-1):
  #print [0+numFacesSectDeb[i], 6+numFacesSectDeb[i], numFacesJoint[i], 7+numFacesJoint[i], 8+numFacesJoint[i],13+numFacesJoint[i]]
  Coques.append(geompy.MakeShell([Faces[0+numFacesSectDeb[i]], Faces[6+numFacesSectDeb[i]],Faces[numFacesJoint[i]], Faces[7+numFacesJoint[i]], Faces[8+numFacesJoint[i]],Faces[13+numFacesJoint[i]]]))
  Coques.append(geompy.MakeShell([Faces[1+numFacesSectDeb[i]], Faces[7+numFacesSectDeb[i]],Faces[1+numFacesJoint[i]], Faces[8+numFacesJoint[i]], Faces[9+numFacesJoint[i]],Faces[12+numFacesJoint[i]]]))
  Coques.append(geompy.MakeShell([Faces[2+numFacesSectDeb[i]], Faces[8+numFacesSectDeb[i]],Faces[6+numFacesJoint[i]], Faces[9+numFacesJoint[i]], Faces[10+numFacesJoint[i]],Faces[13+numFacesJoint[i]]]))
  Coques.append(geompy.MakeShell([Faces[3+numFacesSectDeb[i]], Faces[9+numFacesSectDeb[i]],Faces[2+numFacesJoint[i]], Faces[3+numFacesJoint[i]], Faces[11+numFacesJoint[i]],Faces[12+numFacesJoint[i]]]))
  Coques.append(geompy.MakeShell([Faces[4+numFacesSectDeb[i]], Faces[10+numFacesSectDeb[i]],Faces[4+numFacesJoint[i]], Faces[5+numFacesJoint[i]], Faces[10+numFacesJoint[i]],Faces[11+numFacesJoint[i]]]))
  if (i in Passe):
    Coques.append(geompy.MakeShell([Faces[5+numFacesSectDeb[i]], Faces[11+numFacesSectDeb[i]], Faces[0+numFacesJoint[i]], Faces[14+numFacesJoint[i]], Faces[15+numFacesJoint[i]], Faces[16+numFacesJoint[i]]]))
    #Coques.append(geompy.MakeShell([Faces[5+numFacesSectDeb[i]], Faces[11+numFacesSectDeb[i]], Faces[0+numFacesJoint[i]]_51, Faces[14+numFacesJoint[i]]_65, Faces[15+numFacesJoint[i]]_66, Faces[16+numFacesJoint[i]]_67]))
#Solide_1 = geompy.MakeSolid([Coque_1])
#Face_25 = geompy.MakeFaceWires([Ligne_10, Ligne_27, Ligne_70, Ligne_74], 1)
#Face_26 = geompy.MakeFaceWires([Ligne_11, Ligne_28, Ligne_74, Ligne_76], 1)
#Face_27 = geompy.MakeFaceWires([Ligne_13, Ligne_30, Ligne_75, Ligne_76], 1)
#Face_28 = geompy.MakeFaceWires([Ligne_12, Ligne_29, Ligne_76, Ligne_78], 1)
#Face_29 = geompy.MakeFaceWires([Ligne_14, Ligne_31, Ligne_71, Ligne_76], 1)
#Face_30 = geompy.MakeFaceWires([Ligne_9, Ligne_26, Ligne_73, Ligne_74], 1)

#Face_67 = geompy.MakeFaceWires([Ligne_32, Ligne_49, Ligne_81, Ligne_91], 1)
#Face_68 = geompy.MakeFaceWires([Ligne_33, Ligne_50, Ligne_91, Ligne_92], 1)
#Face_69 = geompy.MakeFaceWires([Ligne_34, Ligne_51, Ligne_82, Ligne_92], 1)
  
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
# for i,sommet in enumerate(Sommets):
#   geompy.addToStudy( sommet, 'Sommet_'+str(i+1) )
# for i,ligne in enumerate(Lignes):
#   geompy.addToStudy( ligne, 'Ligne_'+str(i+1) )
# for i,face in enumerate(Faces):
#       geompy.addToStudy( face, 'Face_'+str(i+1) )
Solides=[]
for i,coque in enumerate(Coques):
  solide = geompy.MakeSolid([coque])
  Solides.append(solide)
#  geompy.addToStudy(solide,'Solide_'+str(i)) 
Eprouv = geompy.MakeCompound(Solides)

Solides = geompy.ExtractShapes(Eprouv, geompy.ShapeType["SOLID"], True)

# 
#   for i in [
# 
#
#
# print 'Ar_te_2',listSameIDs
# geomObj_431 = geompy.GetInPlace(Solide_0, Ar_te_2, True)
geompy.addToStudy(Eprouv,'test')
for i,sol in enumerate(Solides):
  localAretes = geompy.ExtractShapes(sol, geompy.ShapeType["EDGE"], True)
  lsIDS=[]
  for ii in [1,2,9,10]:
     geomObj = geompy.GetInPlace(sol,localAretes[ii], True)
     listSameIDs = geompy.GetSameIDs(sol, geomObj)
     lsIDS.append(listSameIDs[0])
  Groupe = geompy.CreateGroup(sol, geompy.ShapeType["EDGE"])
  geompy.UnionIDs(Groupe, lsIDS)
  geompy.addToStudyInFather(Eprouv,sol,'solide_'+str(i))
  geompy.addToStudyInFather(sol,Groupe,'GroupeLong')
  
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
