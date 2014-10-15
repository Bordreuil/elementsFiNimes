from pylab import *
import numpy

X   = loadtxt('plastsyyn.dat')
ind = numpy.argsort(X,axis=0)

Y  = loadtxt('consyy.dat')
indy = numpy.argsort(Y,axis=0)

plot(X[ind[:,0],0],X[ind[:,0],1],linewidth=3)
plot(Y[indy[:,0],0],Y[indy[:,0],1]*150,'o')
legend(['plastique','elastique'])
xlabel('X en mm')
ylabel('Contrainte yy en MPa')
show()
