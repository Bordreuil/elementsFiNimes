
import geompy
from numpy import *

class poutre:
    def __init__(self,name,sommetDebut,sommetFin):
        self._name        = name
        self._sommetDebut = sommetDebut
        self._sommetFin   = sommetFin
        self._joints      = []
        self._distance    = geompy.MinDistance(sommetDebut,sommetFin)
    def addJoint(self,pourcent):
        if pourcent > 0 and pourcent < 1: 
            self._joints.append(pourcent)
    def addEvenlySpacedJoint(self,distDuDebut,NbJoint,distEntreJoint):
        pourcDebut = distDuDebut/self._distance
        pourcInc   = distEntreJoint/self._distance
        for i in range(NbJoint):
            self.addJoint(pourcDebut+i*pourcInc)
    def build(self):
        joints=list(set(self._joints))
        joints.sort()
        self._sommets=[self._sommetDebut]
        debut =array(geompy.PointCoordinates(self._sommetDebut),'d')
        fin   =array(geompy.PointCoordinates(self._sommetFin),'d')
        vec   = fin-debut
        self._lignes = []
        for i,j in enumerate(joints):
            print j
            coord = debut + vec*j
            self._sommets.append(geompy.MakeVertex(coord[0],coord[1],coord[2]))
            self._lignes.append(geompy.MakeLineTwoPnt(self._sommets[i],
                                                self._sommets[i+1]))
        self._sommets.append(self._sommetFin)
        self._lignes.append(geompy.MakeLineTwoPnt(self._sommets[-2],
                                                self._sommets[-1]))
    def entities(self):
        return  self._sommets,self._lignes
    def sommet(self,num):
        return self._sommets[num]
    def ligne(self,num):
        return self._lignes[num]


def creerPoutresEntre(name,p1,p2,s1Start=0,s2Start=0,Nb=1,incrJoint=1):
    poutres=[]
    for i in range(Nb):
        sp1=p1.sommet(s1Start+i*incrJoint)
        sp2=p2.sommet(s2Start+i*incrJoint)
        poutres.append(poutre(name+'_'+str(i),sp1,sp2))
    return poutres


if __name__=='__main__':
    s1 = geompy.MakeVertex(0.,0.,0.)
    s2 = geompy.MakeVertex(1000.,0.,0.)
    
    p1 = poutre('corniereL',s1,s2)
    p1.addEvenlySpacedJoint(100.,10,50.)
    p1.addJoint(0.05)
    p1.build()
