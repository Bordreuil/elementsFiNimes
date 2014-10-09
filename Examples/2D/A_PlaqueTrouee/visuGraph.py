from pylab import *
import numpy

X   = loadtxt('plastsyyn.dat')
ind = numpy.argsort(X,axis=0)
print ind
print X[ind[:,0],:]
plot(X[ind[:,0],0],X[ind[:,0],1])
xlabel('X en mm')
ylabel('Contrainte yy en MPa')
show()
