# -*- coding: utf-8 -*-

# Copyright Universite Montpellier 2/CNRS 
# Contributor(s) : 
#         Julien Chapuis
#         Cyril Bordreuil
# Contact: cyril.bordreuil@univ-montp2.fr
# 
# This software is a computer program whose purpose is to [describe
#  functionalities and technical features of your software].
#
# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software.  You can  use, 
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability. 
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security. 
# 
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from BAME.modelling.bindings.vtkInterface    import *
from BAME.analysis.tools.PyBameInterpolation import *
from pylab import *
from MEDLoader import *

try :
    from MEDLoader import *
except ImportError:
    print "BAME Message: Pour utilise la lecture de fichier med aster, la librairie 'MEDLoader.py' est necessaire"






#  Attention a la dimension du maillage
class asterMedFile:
    def __init__(self,fichier,nomMaillage='MA'):
        self._fichier     = fichier
        self._nomMaillage = nomMaillage
        self._readMesh()
    def _readMesh(self):
        # On suppose uniquement um maillage de defini
        mesh           = MEDLoader.ReadUMeshFromFile(self._fichier,self._nomMaillage, 0)
        coords         = mesh.getCoords()
        self._nbNodes  = coords.getNumberOfTuples()
        X              = zeros((self._nbNodes,2),'d')

        for i in range(self._nbNodes):
            X[i,0] = coords.getIJ(i,0)
            X[i,1] = coords.getIJ(i,1)

        self._coordsNodes = X
    def numberOfNodes(self):
        return self._nbNodes
    def coordNodes(self):
        return self._coordsNodes
    def nodes(self):
        X=self.coordNodes()
        nodes=dict();
        for j in range(X.shape[0]):
            nodes[j] = Point(X[j,0],X[j,1])
        return nodes
    def timeStepsIds(self,field='TEMP____TEMP'):
        timeStepsIds=MEDLoader.GetNodeFieldIterations(self._fichier,self._nomMaillage,field)
        return timeStepsIds
    def timeAtStep(self,inc,order,field='TEMP____TEMP'):
        return MEDLoader.GetTimeAttachedOnFieldIteration(self._fichier,field,inc,order)
    def times(self,field='TEMP____TEMP'):
        tpsIds = self.timeStepsIds(field)
        tps    = []
        for inc,order in tpsIds:
            tps.append(self.timeAtStep(inc,order,field))
        return tps
    def fieldOnNodes(self,inc,order,field='TEMP____TEMP'):
        champ = MEDLoader.ReadField(ON_NODES,
                            self._fichier,
                            self._nomMaillage,
                            0,
                            field,
                            inc,
                            order)
        nbComp = champ.getNumberOfComponents()
        field  = zeros((self._nbNodes,nbComp),'d')

        for t in range(champ.getNumberOfTuples()):
            for j in range(nbComp):
                field[t,0] = champ.getIJ(t,j)
        return field
