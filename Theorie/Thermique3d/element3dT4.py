# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:40:01 2022

@author: Arthur Giordano
"""
from numpy import *
from matrixTools import *

class Node:
    def __init__(self,num,x,y,z):
        self._id = num
        self._x = x
        self._y = y
        self._z = z
    def x(self):
        return self._x
    def y(self):
        return self._y
    def z(self):
        return self._z
    def id(self):
        return self._id

class Nodes(dict):
    def addNode(self,num,node):
        self[num] = node

class T4Thermal3d:
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
    def gausspoints(self):
        return self._gps
    def weights(self):
        return self._ws
    def setMaterialProperties(self,C):
        self._C = C
    def setGaussPointsAndWeights(self,pts,weights):
        self._gps = pts
        self._ws  = weights
    def conductivity(self):
        return self._C
    def matrixC(self):
        C = self.conductivity()
        C = eye(3) * C
        return C
    def matrixB(self,xi,eta,zeta):
        Dn    = self.Dn(xi,eta,zeta)
        J     = self.jacobian(xi,eta,zeta)
        invJ  = linalg.inv(J)
        B     = dot(invJ,Dn)
        return B
    def computeKT(self):
        pts     = self.gausspoints()
        weights = self.weights()
        KT      = zeros((4,4),'d')

        for i in range(pts.shape[0]):
            B = self.matrixB(pts[i,0],pts[i,1],pts[i,2])
            C = self.matrixC()
            J = self.J(pts[i,0],pts[i,1],pts[i,2])
            KT += dot(transpose(B),dot(C,B))*J/6*weights[i]

        return KT
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
    def jacobian(self,xi,eta,zeta):
        Dn = self.Dn(xi,eta,zeta)
        J  = dot(Dn,self.coordNodes())
        return J

    def J(self,xi,eta,zeta):
        return linalg.det(self.jacobian(xi,eta,zeta))

    def Dn(self,xi,eta,zeta):
        dN = zeros((3,4),'d')
        dN[0,0] = -1. ;dN[0,1] = 1.;dN[0,2] = 0 ;dN[0,3] = 0
        dN[1,0] = -1. ;dN[1,1] = 0 ;dN[1,2] = 1 ;dN[1,3] = 0
        dN[2,0] = -1. ;dN[2,1] = 0 ;dN[2,2] = 0 ;dN[2,3] = 1
        return dN
