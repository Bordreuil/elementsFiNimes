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

class elementBaseThermal:
      def jacobian(self,xi,eta,zeta):
        Dn = self.Dn(xi,eta,zeta)
        J  = dot(Dn,self.coordNodes())
        return J

    def J(self,xi,eta,zeta):
        return linalg.det(self.jacobian(xi,eta,zeta))
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
        KT      = zeros((self.nbDdls(),self.nbDdls()),'d')

        for i in range(pts.shape[0]):
            B = self.matrixB(pts[i,0],pts[i,1],pts[i,2])
            C = self.matrixC()
            J = self.J(pts[i,0],pts[i,1],pts[i,2])
            KT += dot(transpose(B),dot(C,B))*J/6*weights[i]

        return KT

    def computeSource(self,sourceFunction):
        return None
