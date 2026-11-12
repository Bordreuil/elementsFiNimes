from numpy import *
# Intergration H8
GP2 = array([[-1.,-1.,-1],
             [1.,-1.,-1.],
             [1.,1.,-1.],
             [-1.,1.,-1.],
             [-1.,-1.,1],
             [1.,-1.,1.],
             [1.,1.,1.],
             [-1.,1.,1.]],'d')/sqrt(3.)
            
WP2 = ones((8,),'d')

#Integration T10
uq = 1./4.
GP1T10 = array([[uq,uq,uq],],'d')
WP1T10 = array([1./6.],'d')
alpha  = 0.58541020
beta   = 0.13819660
GP4T10 = array([[alpha,beta,beta],[beta,alpha,beta],[beta,beta,alpha],[beta,beta,beta]],'d')
WP4T10 = array([1./24.,1./24.,1./24.,1./24.],'d')

# GP3 = array([-sqrt(3./5.),0.,sqrt(3./5.)],'d')
# WP3 = array([5./9.,8./9.,5./9.],'d')
