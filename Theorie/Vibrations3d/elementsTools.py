from pylab import *
def getNumberOfDofs(coords):
    ntot=coords.shape[0]*3
    return ntot

def computeNonZeroByRows(els,ndofs):
    nnz=ones((ndofs,),'int32')
    for el in els:
        ddls = el.ddls()
        for dof in ddls:
            nnz[dof]+=len(ddls)-1
      
    return nnz
                
