from numpy import *

#GP2 = array([[-1.,-1.,-1],
#             [1.,-1.,-1.],
#             [1.,1.,-1.],
#             [-1.,1.,-1.],
#             [-1.,-1.,1],
#             [1.,-1.,1.],
#             [1.,1.,1.],
#             [-1.,1.,1.]],'d')/sqrt(3.)
a = (5.+3*sqrt(5))/20.
b = (5-sqrt(5))/20.
unsix    = 1./6.
unquatre = 1./4.
undeux   = 1./2.

GP1 = array([[0.25,0.25,0.25]],'d')
WP1 = array([[1.]],'d')



GP2 = array([[a,b,b],
	     [b,b,b],
	     [b,b,a],
	     [b,a,b]],'d')
WP2 = ones((4,),'d')/4.


GP3 = array([[unquatre,unquatre,unquatre],
             [undeux,unsix,unsix],
             [unsix,unsix,unsix],
             [unsix,unsix,undeux],
             [unsix,undeux,unsix]],'d')
WP3 = array([-4./5.,9/20.,9/20.,9/20.,9/20.],'d')
# GP3 = array([-sqrt(3./5.),0.,sqrt(3./5.)],'d')
# WP3 = array([5./9.,8./9.,5./9.],'d')
