from pylab import *

def assembMatrix(K,kel,ddls):
      for i,dd in enumerate(ddls):
        for j,kk in enumerate(ddls):
            K[dd,kk]+=kel[i,j]
      return K

def sliceMatrix(K,ddx,ddy):
    Kout= zeros((len(ddx),len(ddy)))
    for i,dx in enumerate(ddx):
        for j,dy in enumerate(ddy):
            Kout[i,j]=K[dx,dy]
    return Kout

def printMatrix(K):
    for i in range(K.shape[0]):
        ligne=''
        if i ==0:
            ligne+='['
        for j in range(K.shape[1]):
            ligne+=str(K[i,j])+','
        ligne+=']'
        print ligne
