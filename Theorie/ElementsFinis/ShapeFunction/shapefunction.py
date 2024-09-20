from sympy import *

xi   = Symbol('xi')
eta  = Symbol('eta')
zeta = Symbol('zeta')

N =(1. - xi - eta - zeta)*(1.-2.*xi-2.*eta-2.*zeta)

dNdxi=diff(N,xi)
print(dNdxi)
dNdeta=diff(N,eta)
print(dNdeta)
dNdzeta=diff(N,zeta)
print(dNdzeta)
