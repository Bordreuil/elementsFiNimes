from numpy import *

GP2 = array([[-1.,-1.,-1],
             [1.,-1.,-1.],
             [1.,1.,-1.],
             [-1.,1.,-1.],
             [-1.,-1.,1],
             [1.,-1.,1.],
             [1.,1.,1.],
             [-1.,1.,1.]],'d')/sqrt(3.)
            
WP2 = ones((8,),'d')

# GP3 = array([-sqrt(3./5.),0.,sqrt(3./5.)],'d')
# WP3 = array([5./9.,8./9.,5./9.],'d')