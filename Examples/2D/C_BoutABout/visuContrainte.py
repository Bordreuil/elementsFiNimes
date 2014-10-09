from pylab import *

datas = loadtxt('contapo.dat')
X     = datas[:,:2]

th    = arctan2(X[-1,1],X[-1,0])-pi/2.
ind   = X[:,0].argsort()
X     = X[ind,:]

SIXX  = datas[ind,2]
SIYY  = datas[ind,3]
SIXY  = datas[ind,4]

sigma = [] 
for i in range(SIXX.shape[0]):
    sigma.append(array([[SIXX[i],SIXY[i]],
                        [SIXY[i],SIYY[i]]],'d'))


sigma    = array(sigma,'d')             # Contrainte pour tous les points
normal   = array([cos(th),sin(th)],'d') # normal a la facette
tangente =  array([cos(th+pi/2.),
                   sin(th+pi/2.)],'d')# tangente a la facette
vCont    = dot(sigma,normal)            # vecteur contrainre

snormal  = dot(vCont,normal)            # contrainte normale a la facette
stangent = dot(vCont,tangente)          # contrainte tangentiel a la facette

sigeq    = sqrt(snormal**2.+3.*stangent**2.)

plot(X[:,0],snormal,'^-',
     X[:,0],stangent,'o-',
     X[:,0],sigeq,
     linewidth=2,markersize=8)
legend(['Contrainte normale','Contrainte tangentielle','Contrainte equivalente'])
show()
