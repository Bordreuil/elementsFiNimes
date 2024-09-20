# -*- coding: utf-8 -*-
from elementBase import *

class T4Thermal3d(elementBaseThermal):
    def __init__(self,n1,n2,n3,n4):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
        self._n4 = n4
    def connectivite(self):
        return [self._n1.id(),self._n2.id(),self._n3.id(),self._n4.id()]
    def ddls(self):
        ddls=[]
        for i in self.connectivite():
                ddls.append(i)
        return array(ddls,'int32')
    def coordNodes(self):
        coord      = zeros((4,3),'d')
        coord[0,:] = [self._n1.x(),self._n1.y(),self._n1.z()]
        coord[1,:] = [self._n2.x(),self._n2.y(),self._n2.z()]
        coord[2,:] = [self._n3.x(),self._n3.y(),self._n3.z()]
        coord[3,:] = [self._n4.x(),self._n4.y(),self._n4.z()]
        return coord

    def N(self,xi,eta,zeta):
        N    = array((4,),'d')
        N[0] = 1. - xi - eta - zeta
        N[1] = xi
        N[2] = eta
        N[3] = zeta
        return N

    def Dn(self,xi,eta,zeta):
        dN = zeros((3,4),'d')
        dN[0,0] = -1. ;dN[0,1] = 1.;dN[0,2] = 0 ;dN[0,3] = 0
        dN[1,0] = -1. ;dN[1,1] = 0 ;dN[1,2] = 1 ;dN[1,3] = 0
        dN[2,0] = -1. ;dN[2,1] = 0 ;dN[2,2] = 0 ;dN[2,3] = 1
        return dN
