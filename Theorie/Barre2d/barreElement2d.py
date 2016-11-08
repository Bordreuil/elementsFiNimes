from pylab import *
from numpy import *

class barre2D:
    def __init__(self,nodes,L,E,A,th):
        self._nodes  = nodes
        self._length = L
        self._young  = E
        self._surf   = A
        self._th     = th
    def ddls(self):
        return [self._nodes[0]*2,
                self._nodes[0]*2+1,
                self._nodes[1]*2,
                self._nodes[1]*2+1]
    def connectivite(self):
        return [self._nodes[0],self._nodes[1]]
    def matricePassage(self):
        th = self._th
        Q=zeros((4,4),'d')
        q=array([[cos(th),sin(th)],
                 [-sin(th),cos(th)]],'d')
        Q[0:2,0:2]=q;Q[2:,2:]=q
        return Q
    def calculContrainte(self,dep):
        Q=self.matricePassage()
        duloc=dot(Q,dep)
        deformation=(duloc[2]-duloc[0])/self._length
        return self._young*deformation
    def stiffness(self):
    
        E  = self._young
        A  = self._surf
        L  = self._length
        k  = zeros((4,4),'d')
        k[0,0]= 1. ;k[0,2]=-1.
        k[2,0]= -1.;k[2,2]=1.
        Q=self.matricePassage()
        K=E*A/L*dot(transpose(Q),dot(k,Q))
        return K
