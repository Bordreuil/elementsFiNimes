# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:40:01 2022

@author: Arthur Giordano
"""
from elementBase import *

class T10Thermal3d(elementBaseThermal):
    def __init__(self,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
        self._n4 = n4
        self._n5 = n5
        self._n6 = n6
        self._n7 = n7
        self._n8 = n8
        self._n9 = n10
        self._n9 = n10
    def nbDdls(self):
        return 10
  
    def connectivite(self):
        return [self._n1.id(),self._n2.id(),self._n3.id(),self._n4.id(),
                self._n5.id(),self._n6.id(),self._n7.id(),self._n8.id(),
                self._n9.id(),self._n10.id()]    
    def coordNodes(self):
        coord      = zeros((10,3),'d')
        coord[0,:] = [self._n1.x(),self._n1.y(),self._n1.z()]
        coord[1,:] = [self._n2.x(),self._n2.y(),self._n2.z()]
        coord[2,:] = [self._n3.x(),self._n3.y(),self._n3.z()]
        coord[3,:] = [self._n4.x(),self._n4.y(),self._n4.z()]
        coord[4,:] = [self._n5.x(),self._n5.y(),self._n5.z()]
        coord[5,:] = [self._n6.x(),self._n6.y(),self._n6.z()]
        coord[6,:] = [self._n7.x(),self._n7.y(),self._n7.z()]
        coord[7,:] = [self._n8.x(),self._n8.y(),self._n8.z()]
        coord[8,:] = [self._n9.x(),self._n9.y(),self._n9.z()]
        coord[9,:] = [self._n10.x(),self._n10.y(),self._n10.z()]
  
        return coord

    def N(self,xi,eta,zeta):
        N    = array((10,),'d')
        N[0] = (1. - xi - eta - zeta)*(1.-2.*xi-2.*eta-2.*zeta)
        N[1] = xi*(2.*xi-1)
        N[2] = eta*(2.*eta-1)
        N[3] = zeta*(2.*zeta-1)
        N[4] = 4.*xi*(1. - xi - eta - zeta)
        N[5] = 4.*eta*(1. - xi - eta - zeta)
        N[6] = 4.*zeta*(1. - xi - eta - zeta)
        N[7] = 4.*xi*eta
        N[8] = 4.*zeta*eta
        N[9] = 4.*xi*zeta

        return N
    # FINIR le Dn
    def Dn(self,xi,eta,zeta):
        dN = zeros((3,10),'d')
        dN[0,0] = -1. ;dN[0,1] = 1.;dN[0,2] = 0 ;dN[0,3] = 0;dN[0,4] =
        dN[0,5] = -1. ;dN[0,6] = 1.;dN[0,7] = 0 ;dN[0,8] = 0;dN[0,9] =
        dN[1,0] = -1. ;dN[1,1] = 1.;dN[1,2] = 0 ;dN[1,3] = 0;dN[1,4] =
        dN[1,5] = -1. ;dN[1,6] = 1.;dN[1,7] = 0 ;dN[1,8] = 0;dN[1,9] =
        dN[2,0] = -1. ;dN[2,1] = 1.;dN[2,2] = 0 ;dN[2,3] = 0;dN[2,4] =
        dN[2,5] = -1. ;dN[2,6] = 1.;dN[2,7] = 0 ;dN[2,8] = 0;dN[2,9] =

        return dN



 
