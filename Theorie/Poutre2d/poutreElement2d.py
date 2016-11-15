from pylab import *
from numpy import *

class poutre2D:
    def __init__(self,nodes,L,E,A,I,th):
        self._nodes  = nodes
        self._length = L
        self._young  = E
        self._surf   = A
        self._I      = I
        self._th     = th
    def ddls(self):
        return [self._nodes[0]*3,
                self._nodes[0]*3+1,
                self._nodes[0]*3+2,
                self._nodes[1]*3,
                self._nodes[1]*3+1,
                self._nodes[1]*3+2   ]
    def connectivite(self):
        return [self._nodes[0],self._nodes[1]]
    def matricePassage(self):
        th = self._th
        Q=zeros((6,6),'d')
        q=array([[cos(th),sin(th),0],
                 [-sin(th),cos(th),0.],
                 [0.,0.,1.]],'d')
        Q[0:3,0:3]=q;Q[3:,3:]=q
        return Q
    def calculContrainteTraction(self,dep):
        Q=self.matricePassage()
        duloc=dot(Q,dep)
        deformation=(duloc[3]-duloc[0])/self._length
        return self._young*deformation
    def stiffness(self):
    
        E  = self._young
        A  = self._surf
        I  = self._I
        L  = self._length
        Ct = A*L**2/I
        k  = E*I/L**3.*array([[Ct ,0.  ,0.      ,-Ct ,0.   ,0.],
                              [0. ,12. ,6*L     ,0.  ,-12  ,6.*L],
                              [0. ,6.*L,4.*L**2.,0.  ,6.*L ,2.*L**2.],
                              [-Ct,0.  ,0.      ,Ct  ,0.   ,0.    ],
                              [0.,-12.,-6.*L    ,0.  ,12.  , -6.*L],
                              [0.,6.*L,2.*L**2  ,0.  ,-6.*L,4.*L**2.]],'d')
        Q=self.matricePassage()
        K=dot(transpose(Q),dot(k,Q))
        return K
