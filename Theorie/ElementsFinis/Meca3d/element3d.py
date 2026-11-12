from numpy import *
from matrixTools import *
from abc import ABC,abstractmethod

HEXAHEDRON  = 'Hexahedre'
TETRAHEDRON = 'Tetrahedre'

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
    
class Element3d(ABC):
    @abstractmethod
    def connectivite(self):
       pass
    @abstractmethod
    def coordNodes(self):
        pass
    @abstractmethod
    def N(self,r,s,q):
        pass
    @abstractmethod
    def Dn(self,r,s,q):
        pass
    @abstractmethod
    def type(self):
        pass
    @abstractmethod
    def summits(self):
        pass
    
    def numberOfNodes(self):
        return len(self.connectivite())
    def numberOfDdls(self):
        return len(self.ddls())
    def ddls(self):
        ddls=[]
        for i in self.connectivite():
            for j in range(3):
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
        Em = zeros((6,6),'d')
        E  = self.young()
        nu = self.poisson()
        Cp = E/(1+nu)/(1.-2.*nu)
        G  = E/2./(1.+nu)
        Em[0,0] =  (1.-nu)*Cp       ; Em[0,1] = nu*Cp ; Em[0,2] = nu*Cp 
        Em[1,0] =  nu*Cp    ; Em[1,1] = (1.-nu)*Cp    ; Em[1,2] = nu*Cp
        Em[2,0] =  nu*Cp    ; Em[2,1] = Cp*nu ; Em[2,2] = (1.-nu)*Cp
        Em[3,3] =  G;
        Em[4,4] =  G;
        Em[5,5] =  G;
        return Em
    
    def matrixB(self,r,s,q):
        Dn    = self.Dn(r,s,q)
        deriv = zeros((9,self.numberOfDdls()),'d')
        J     = self.jacobian(r,s,q)
        deriv[0:3,::3]  = dot(linalg.inv(J),Dn)
        deriv[3:6,1::3] = dot(linalg.inv(J),Dn)
        deriv[6:,2::3]  = dot(linalg.inv(J),Dn)
        passDef = zeros((6,9),'d')
        passDef[0,0] = 1.;passDef[1,4] = 1.;passDef[2,8]=1.;
        passDef[3,1]=1.;passDef[3,3]=1.
        passDef[4,5]=1.;passDef[4,7]=1.
        passDef[5,2]=1.;passDef[5,6]=1.
        B = dot(passDef,deriv)
        return B
    def stiffness(self):
        K =zeros((self.numberOfDdls(),self.numberOfDdls()),'d')
        pts    = self.gausspoints()
        weights = self.weights()
        for i in range(pts.shape[0]):
            B = self.matrixB(pts[i,0],pts[i,1],pts[i,2])
            E = self.matrixE()
            J = self.J(pts[i,0],pts[i,1],pts[i,2])
            K+=dot(transpose(B),dot(E,B))*weights[i]*J
  
        return K
 
    def jacobian(self,r,s,q):
        Dn = self.Dn(r,s,q)
        J  = dot(Dn,self.coordNodes())
        return J
    def J(self,r,s,q):
        return linalg.det(self.jacobian(r,s,q))
    def computeStressesInElement(self,du):
        sigmas = self._computeStressesAtGaussPoints(du)
        sigma  = 0
        for i in range(len(self.weights())):
            sigma+=sigmas[i]*self.weights()[i]
        return sigma/8
    def _computeStressesAtGaussPoints(self,du):
        pts = self.gausspoints()
        stressesAtGP=zeros((pts.shape[0],6),'d')
        E = self.matrixE()
        for i in range(pts.shape[0]):
            B = self.matrixB(pts[i,0],pts[i,1],pts[i,2])
            stressesAtGP[i,:] = dot(E,dot(B,du))
        return stressesAtGP
    
class H8Meca3d(Element3d):
    def __init__(self,n1,n2,n3,n4,n5,n6,n7,n8):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
        self._n4 = n4
        self._n5 = n5
        self._n6 = n6
        self._n7 = n7
        self._n8 = n8
    def connectivite(self):
        return [self._n1.id(),self._n2.id(),self._n3.id(),self._n4.id(),self._n5.id(),self._n6.id(),self._n7.id(),self._n8.id()]
    def summits(self):
        return self.connectivite()
    def type(self):
        return HEXAHEDRON
    def coordNodes(self):
        coord      = zeros((8,3),'d')
        coord[0,:] = [self._n1.x(),self._n1.y(),self._n1.z()]
        coord[1,:] = [self._n2.x(),self._n2.y(),self._n2.z()]
        coord[2,:] = [self._n3.x(),self._n3.y(),self._n3.z()]
        coord[3,:] = [self._n4.x(),self._n4.y(),self._n4.z()]
        coord[4,:] = [self._n5.x(),self._n5.y(),self._n5.z()]
        coord[5,:] = [self._n6.x(),self._n6.y(),self._n6.z()]
        coord[6,:] = [self._n7.x(),self._n7.y(),self._n7.z()]
        coord[7,:] = [self._n8.x(),self._n8.y(),self._n8.z()]
        return coord
    
    def N(self,r,s,q):
        N = array((8,),'d')
        N[0] = 1./8.*(1.-r)*(1.-s)*(1.-q)
        N[1] = 1./8.*(1.+r)*(1.-s)*(1.-q)
        N[2] = 1./8.*(1.+r)*(1.+s)*(1.-q)
        N[3] = 1./8.*(1.-r)*(1.+s)*(1.-q)
        N[4] = 1./8.*(1.-r)*(1.-s)*(1.+q)
        N[5] = 1./8.*(1.+r)*(1.-s)*(1.+q)
        N[6] = 1./8.*(1.+r)*(1.+s)*(1.+q)
        N[7] = 1./8.*(1.-r)*(1.+s)*(1.+q)
        return N

    def Dn(self,r,s,q):
        dN = zeros((3,8),'d')
        # A VERIFIER
        dN[0,0] = -1./8.*(1.-s)*(1.-q);
        dN[1,0] = -1./8.*(1.-r)*(1.-q);
        dN[2,0] = -1./8.*(1.-r)*(1.-s);
        dN[0,1] = 1./8.*(1.-s)*(1.-q);
        dN[1,1] = -1./8.*(1.+r)*(1.-q);
        dN[2,1] = -1./8.*(1.+r)*(1.-s);
        dN[0,2] = 1./8.*(1.+s)*(1.-q);
        dN[1,2] = 1./8.*(1.+r)*(1.-q);
        dN[2,2] = -1./8.*(1.+r)*(1.+s);
        dN[0,3] = -1./8.*(1.+s)*(1.-q);
        dN[1,3] = 1./8.*(1.-r)*(1.-q);
        dN[2,3] = -1./8.*(1.-r)*(1.+s);
        dN[0,4] = -1./8.*(1.-s)*(1.+q);
        dN[1,4] = -1./8.*(1.-r)*(1.+q);
        dN[2,4] = 1./8.*(1.-r)*(1.-s);
        dN[0,5] = 1./8.*(1.-s)*(1.+q);
        dN[1,5] = -1./8.*(1.+r)*(1.+q);
        dN[2,5] = 1./8.*(1.+r)*(1.-s);
        dN[0,6] = 1./8.*(1.+s)*(1.+q);
        dN[1,6] = 1./8.*(1.+r)*(1.+q);
        dN[2,6] = 1./8.*(1.+r)*(1.+s);
        dN[0,7] = -1./8.*(1.+s)*(1.+q);
        dN[1,7] = 1./8.*(1.-r)*(1.+q);
        dN[2,7] = 1./8.*(1.-r)*(1.+s);
        return dN

class T10Meca3d(Element3d):
    def __init__(self,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
        self._n4 = n4
        self._n5 = n5
        self._n6 = n6
        self._n7 = n7
        self._n8 = n8
        self._n9 = n9
        self._n10 = n10
    def type(self):
        return TETRAHEDRON
    def summits(self):
         return [self._n1.id(),self._n2.id(),self._n3.id(),self._n4.id()]
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
    
    def N(self,r,s,q):
        N = array((10,),'d')
        L4 = 1.-r-s-q
        N[0] = (2*r-1)*r
        N[1] = (2*s-1)*s
        N[2] = (2*q-1)*q
        N[3] = (2*L4-1)*L4
        N[4] = 4.*r*s
        N[5] = 4.*s*q
        N[6] = 4*q*r
        N[7] = 4.*r*L4
        N[8] = 4.*s*L4
        N[9] = 4.*q*L4
 
        return N

    def Dn(self,r,s,q):
        dN = zeros((3,10),'d')
        L4 = 1.-r-s-q
        # A VERIFIER
        dN[0,0] = 4.*r-1;
        dN[1,0] = 0;
        dN[2,0] = 0;
        dN[0,1] = 0.;
        dN[1,1] = 4.*s-1;
        dN[2,1] = 0.;
        dN[0,2] = 0.;
        dN[1,2] = 0.;
        dN[2,2] = 4.*q-1;
        dN[0,3] = -4*L4+1;  
        dN[1,3] = -4*L4+1;   
        dN[2,3] = -4*L4+1;  
        dN[0,4] = 4.*s;
        dN[1,4] = 4.*r;
        dN[2,4] = 0;
        dN[0,5] = 0.;
        dN[1,5] = 4.*q;
        dN[2,5] = 4.*s;
        dN[0,6] = 4.*q;
        dN[1,6] = 0.;      
        dN[2,6] = 4.*r;    
        dN[0,7] = 4*L4-4.*r;     
        dN[1,7] = -4.*r;      
        dN[2,7] = -4.*r;     
        dN[0,8] = -4.*s;      
        dN[1,8] = 4.*L4-4*s;      
        dN[2,8] = -4.*s;
        dN[0,9] = -4*q;
        dN[1,9] = -4*q;
        dN[2,9] = 4.*L4-4.*q;     
       
        return dN

class T4Meca3d(Element3d):
    def __init__(self,n1,n2,n3,n4):
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
        self._n4 = n4
    def type(self):
        return TETRAHEDRON
    def summits(self):
        return self.connectivite()
    def connectivite(self):
        return [self._n1.id(),self._n2.id(),self._n3.id(),self._n4.id()]
        
    def coordNodes(self):
        coord      = zeros((4,3),'d')
        coord[0,:] = [self._n1.x(),self._n1.y(),self._n1.z()]
        coord[1,:] = [self._n2.x(),self._n2.y(),self._n2.z()]
        coord[2,:] = [self._n3.x(),self._n3.y(),self._n3.z()]
        coord[3,:] = [self._n4.x(),self._n4.y(),self._n4.z()]
        return coord
    
    def N(self,r,s,q):
        N = array((4,),'d')
        N[0] = r
        N[1] = s
        N[2] = q
        N[3] = 1.-r-s-q
 
        return N

    def Dn(self,r,s,q):
        dN = zeros((3,4),'d')
        # A VERIFIER
        dN[0,0] = 1;
        dN[1,0] = 0;
        dN[2,0] = 0;
        dN[0,1] = 0.;
        dN[1,1] = 1.;
        dN[2,1] = 0.;
        dN[0,2] = 0.;
        dN[1,2] = 0.;
        dN[2,2] = 1.;
        dN[0,3] = -1;
        dN[1,3] = -1;
        dN[2,3] = -1.;
       
        return dN
