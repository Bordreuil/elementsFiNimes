# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:30:03 2023

@author: Arthur Giordano
"""

import sys
import numpy as np
from readDat_modif     import *
from element3dT4   import *
from pointsGauss import *
from matrixTools import *
from visuTools   import *

C         = 1.

filename = 'Cube_T4'

nodes,els = readDat_modifT4Thermal('datas/' + filename +'_cyril_pf.dat')

nnodes     = len(nodes)
ndofs      = nnodes
print("Nombre noeuds :",nnodes, "& nombre dof :", ndofs)

nodeCL_Lower   = readDat_modifT4Thermal('datas/' + filename +'_CL_Lower_cyril_pf.dat')
CL_Lower       = [x.id() for x in nodeCL_Lower[0].values()]

nodeCL_Upper   = readDat_modifT4Thermal('datas/' + filename +'_CL_Upper_cyril_pf.dat')
CL_Upper       = [x.id() for x in nodeCL_Upper[0].values()]

imposedDofs    = []
imposedValues  = []

for nd in CL_Lower:
    imposedDofs.append(nd)
    imposedValues.append(20)
for nd in CL_Upper:
    imposedDofs.append(nd)
    imposedValues.append(100)

print(imposedDofs)
print(imposedValues)

Kglob=zeros((ndofs,ndofs),'d')
Fglob=zeros((ndofs,1),'d')

tdeb   = time.time()
print('....Debut d assemblage')
for el in els:
    el.setMaterialProperties(C)
    el.setGaussPointsAndWeights(GP2,WP2)
    kel   = el.computeKT()
    ddls  = el.ddls()
    Kglob = assembMatrix(Kglob,kel,ddls)

print('....Fin d assemblage')

print('....DiricletCondition')
#
#T = zeros((nnodes,1))

Kprob,Fprob  = imposedDofsOnMatrixAndRhs(Kglob,Fglob,imposedDofs,imposedValues)
#Kprob,Fprob = imposedDofsOnMatrixAndRhs(Kprob,Fprob,imposedDofs_Lower,values_Lower)
print('Resolution')
# Solve for the global temperatures at the free degrees of freedom
tu = linalg.solve(Kprob,Fprob)
#print('tempU',tu)

nn = list(nodes.keys())
nn.sort()
print(nn)
xx = [nodes[n].z() for n in nn]
plot(xx,tu,'o')
show()
print('------Resolution en:',time.time()-tdeb,' s')
print('....Ecriture des resultats')
resFile = resultsFileT4Thermal(filename + '_Temp.vtu')
resFile.defineMesh(nodes,els)
resFile.addVectorToNode(tu ,'TEMP')
resFile.write()
