from pylab import *

def dofNumberGlobal(node,ddl):
      """
      donne le numero de dll global en fonction du noeud et du ddl sur x (0) ou y (1) ou z(2)
      """
      return node*3+ddl

def nodeDdlNumber(dof):
      """
      donne le noeud et le ddl local en fonction du ddl global
      """
      nnode =  floor(dof/3)
      return int(nnode),int(dof-nnode*3)

def listActiveDofs(nddls,dofsImposed):
      """
      ressort la liste des ddls actifs
      """
      ddlsActive = []
      for i in range(nddls):
            if i not in dofsImposed:
                  ddlsActive.append(i)
      return ddlsActive

def assembMatrix(K,kel,ddls):
      """
      Realise l assemblage de la matrice elementaire
      dans la matrice globale pour les ddls
      """
      for i,dd in enumerate(ddls):
        for j,kk in enumerate(ddls):
            K[dd,kk] += kel[i,j]
      return K

def sliceMatrix(K,ddx,ddy):
    """
    """
    Kout= zeros((len(ddx),len(ddy)))
    for i,dx in enumerate(ddx):
        for j,dy in enumerate(ddy):
            Kout[i,j] = K[dx,dy]
    return Kout
def imposedDofsOnMatrixAndRhs(K,F,ddlsImposed,values):
      """
      Impose des ddls avec certaines valeurs en modifiant la 
      matrice de rigidite globale
      """
      assert(len(values)==len(ddlsImposed))
      for ii,i in enumerate(ddlsImposed):
            K[i,:] = 0.
            K[i,i] = 1.
            F[i]   = values[ii]
      return K,F
def printMatrix(K):
    for i in range(K.shape[0]):
        ligne=''
        if i ==0:
            ligne+='['
        for j in range(K.shape[1]):
            ligne+='\t'+str(K[i,j])+','
        ligne+=']'
        print(ligne)
