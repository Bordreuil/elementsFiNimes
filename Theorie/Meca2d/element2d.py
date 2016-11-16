from numpy import *
from matrixTools import *
class Node:
    def __init__(self,num,x,y):
        self._id = num
        self._x = x
        self._y = y
    def x(self):
        return self._x
    def y(self):
        return self._y
    def id(self):
        return self._id
    
class Nodes(dict):
    def addNode(self,num,node):
        self[num] = node
    
class TriangleMeca2d:
    def __init__(self,n1,n2,n3):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
    def connectivite(self):
        return [self._n1.id(),self._n2.id(),self._n3.id()]
    def ddls(self):
        ddls=[]
        for i in self.connectivite():
            for j in range(2):
                ddls.append(dofNumberGlobal(i,j))
        return ddls
    def gausspoints(self):
        return self._gps
    def weights(self):
        return self._ws
    def setMaterialProperties(self,E,nu):
        self._E  = E
        self._nu = nu
    def setGaussPointsAndWeights(self,pts,weights):
        self._gps = pts
        self._ws  = weights
    def young(self):
        return self._E

    def poisson(self):
        return self._nu
    def matrixE(self):
        Em = zeros((3,3),'d')
        E  = self.young()
        nu = self.poisson()
        Cp = E/(1-nu**2)
        Em[0,0] =  Cp       ; Em[0,1] = nu*Cp
        Em[1,0] =  nu*Cp    ; Em[1,1] = Cp
        Em[2,2] =  Cp*(1+nu);
        return Em
    def matrixB(self,r,s):
        Dn    = self.Dn(r,s)
        deriv = zeros((4,6),'d')
        J     = self.jacobian(r,s)
        deriv[0:2,::2] = dot(linalg.inv(J),Dn)
        deriv[2:,1::2] = dot(linalg.inv(J),Dn)
        passDef = zeros((3,4),'d')
        passDef[0,0] = 1.;passDef[1,3] = 1.;passDef[2,1]=1.;passDef[2,2]=1.
        B = dot(passDef,deriv)
        return B
    def stiffness(self):
        K =zeros((6,6),'d')
        pts = self.gausspoints()
        weights = self.weights()
        for i in range(pts.shape[0]):
            B = self.matrixB(pts[i,0],pts[i,1])
            E = self.matrixE()
            J = self.J(pts[i,0],pts[i,1])
            K+=dot(transpose(B),dot(E,B))*weights[i]*J
        return K
        
    def coordNodes(self):
        coord      = zeros((3,2),'d')
        coord[0,:] = [self._n1.x(),self._n1.y()]
        coord[1,:] = [self._n2.x(),self._n2.y()]
        coord[2,:] = [self._n3.x(),self._n3.y()]
        return coord
    
    def N(self,r,s):
        N = array((3,),'d')
        N[0] = 1.-r-s
        N[1] = r
        N[2] = s
        return N
    def jacobian(self,r,s):
        Dn = self.Dn(r,s)
        J = dot(Dn,self.coordNodes())
        return J
    def J(self,r,s):
        return linalg.det(self.jacobian(r,s))
    def Dn(self,r,s):
        dN = zeros((2,3),'d')

        dN[0,0] = -1.;dN[0,1] = 1.;dN[0,2] = 0.
        dN[1,0] = -1.;dN[1,1] = 0.;dN[1,2] = 1.
        
        return dN
