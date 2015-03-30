from bidonChar     import * 
from bidonCommBase import *
availablePiquageType = ['Gauche','Droite']
import re
class geompyObjectInterface:
    def geompyObject(self):
        return self._obj
    def setGeompyObject(self,obj):
        self._obj = obj
    def setBrideObject(self,obj):
        self._brideObj = obj
    def brideObject(self):
        return self._brideObj
class piquageVirole(geompyObjectInterface):
    def __init__(self,nom,Hpiquage,Dpiquage,Alpha,Position,Dbride,epaisseur=2.,epaisseurBride=10.,geomPy=None):
        self._geompy = geomPy
        self._nom      = nom
        num     = re.findall('\d+',nom)[0]
        self._nomBride = 'Bride'+num
        self._hpiquage = Hpiquage
        self._dpiquage = Dpiquage
        self._alpha    = Alpha
        self._position = Position
        self._dbride   = Dbride
        self._epaisseur= epaisseur
        self._epBride  = epaisseurBride
        self.buildGeompyObject()
    def name(self):
        return self._nom
    def epaisseur(self):
        return self._epaisseur
    def epaisseurBride(self):
        return self._epBride
    def nameBride(self):
        return self._nomBride
    def Rpiquage(self):
        return self._dpiquage/2.
    def Alpha(self):
        return self._alpha
    def buildGeompyObject(self):
        piq,bride=creerPiquageVirole(self._position,self._hpiquage,self._alpha,self._dpiquage,self._dbride,self._geompy)
        self.setGeompyObject(piq)
        self.setBrideObject(bride)
    def onPositiveSide(self):
        return self._position > 0.
    
class piquageAxialFond(geompyObjectInterface):
    def __init__(self,nom,Type,Hauteur,Rpiquage,Alpha,Dpiquage,Dbride,epaisseur=2.,epBride=10.,geomPy=None):
        self._geompy=geomPy
        self._nom      = nom
        num     = re.findall('\d+',nom)[0]
        self._nomBride = 'Bride'+num
        if Type in availablePiquageType:
            self._type     = Type
        else:
            msg = 'Attention le type de piquage doit etre dans la liste:'
            for t in availablePiquageType:
                msg+=str(t)
            print msg
            self._type = availablePiquageType[0]
        self._hauteur  = Hauteur
        self._rpiquage = Rpiquage
        self._alpha    = Alpha
        self._dpiquage = Dpiquage
        self._dbride   = Dbride
        self._epaisseur= epaisseur
        self._epBride  = epBride
        self.buildGeompyObject()
    def epaisseur(self):
        return self._epaisseur
    def epaisseurBride(self):
        return self._epBride
    def RPosition(self):
        return self._rpiquage
    def RPiquage(self):
        return self._dpiquage/2.
    def Alpha(self):
        return self._alpha
    def Xp(self):
        return self._rpiquage*cos(self._alpha)
    def Yp(self):
        return  self._rpiquage*sin(self._alpha)
    def name(self):
        return self._nom
    def nameBride(self):
        return self._nomBride
    def buildGeompyObject(self):
        if self._type == 'Gauche':
            piq,brid =creerPiquageFondAxialNeg(self._hauteur,
                                                          self._rpiquage,
                                                          self._alpha,
                                                          self._dpiquage,
                                                          self._dbride,self._geompy)
            self.setGeompyObject(piq)
            self.setBrideObject(brid)
        if self._type == 'Droite':
            piq,brid = creerPiquageFondAxialPos(self._hauteur,
                                                          self._rpiquage,
                                                          self._alpha,
                                                          self._dpiquage,
                                                          self._dbride,self._geompy)
            self.setGeompyObject(piq)
            self.setBrideObject(brid)

class bidonFondGRC:
    def __init__(self,Dvirole      = 500.,
                      Lvirole      = 1200.,
                      PositionPieds= 1280.,
                      LargeurPieds = 900.,
                      largeurPieds = 300.,
                      HauteurPieds = 800.,
                      eVirole      = 3.,
                      eFond        = 3.,
                      geomPy       = None):
        self._geompy        = geomPy
        self._Dvirole       = Dvirole
        self._Lvirole       = Lvirole
        self._PositionPieds = PositionPieds
        self._LargeurPieds  = LargeurPieds
        self._largeurPieds  = largeurPieds
        self._HauteurPieds  = HauteurPieds
        self._eVirole       = eVirole
        self._eFond         = eFond

        OX                  = self._geompy.MakeVectorDXDYDZ(1, 0, 0)
        self._Axe           = OX
        Virole,FondG,FondD  = creerViroleEtDeuxGRC(Lvirole,Dvirole,OX,self._geompy)
        Pied1,Pied2         = creerPiedsEnU(PositionPieds,
                                            largeurPieds,
                                            LargeurPieds,
                                            HauteurPieds,
                                            Dvirole,self._geompy)

       
        Corps = self._geompy.MakeCompound([Virole,
                                             FondG,
                                             FondD])
        Virole,Pieds  = couperPiedEtBidon(Pied1,Pied2,Corps,self._geompy)
        self._virole  = Virole
        self._fondG   = FondG
        self._fondD   = FondD 
        self._pieds   = Pieds
        self._piquages = []
        self._updateCorps()

    def _updateCorps(self):
         self._Corps  = self._geompy.MakeCompound([self._virole,
                                             self._fondG,
                                             self._fondD])
    def ajouterPiquageVirole(self,nom,Hpiquage,Dpiquage,Alpha,Position,Dbride):
        Piq2          = piquageVirole(nom,Hpiquage,Dpiquage,Alpha,Position,Dbride,geomPy=self._geompy)

        if Piq2.onPositiveSide():
            if (self.intersectOnMiddle(Piq2)):
                Virole,Piq    = couperVirolePiquagePosCas1(Piq2.geompyObject(),self._Corps,self._geompy)
                self._virole  = Virole
                print 'Virole Pos --  cas 1'
            else:
                Virole,Piq    = couperVirolePiquagePosCas2(Piq2.geompyObject(),self._Corps,self._geompy)
                self._virole  = Virole
                print 'Virole Pos --  cas 2'
            Piq2.setGeompyObject(Piq)
        else:
            if (self.intersectOnMiddle(Piq2)):
                Virole,Piq    = couperVirolePiquageNegCas1(Piq2.geompyObject(),self._Corps,self._geompy)
                self._virole  = Virole
                print 'Virole Neg -- cas 1'
            else:
                Virole,Piq    = couperVirolePiquageNegCas2(Piq2.geompyObject(),self._Corps,self._geompy)
                self._virole  = Virole
                print 'Virole Pos -- Cas 2'
            Piq2.setGeompyObject(Piq)           

        self._updateCorps()
        self._piquages.append(Piq2)
    def intersectOnMiddle(self,Piq):
        return self._Dvirole/2.*sin(Piq.Alpha()) < Piq.Rpiquage()

    def ajouterPiquageAxialFond(self,nom,typ,Hpiquage,Dpiquage,Alpha,Rpiquage,Dbride):
        Piq3          = piquageAxialFond(nom,typ,Hpiquage,Rpiquage,Alpha,Dpiquage,Dbride,geomPy=self._geompy)  
        cas           = self.piquageAxialCase(Piq3)
        print 'Piquage Axial -- Cas :', cas, ' Fond', typ
        if(typ == 'Gauche'):
            if cas in (1,2):
              FondG,Piq=couperFondPiquageNegCas1Ou2(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondG = FondG
              Piq3.setGeompyObject(Piq)
            if cas == 3:
              FondG,Piq=couperFondPiquageNegCas3(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondG = FondG
              Piq3.setGeompyObject(Piq)
            if cas == 4:
              FondG,Piq=couperFondPiquageNegCas4(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondG = FondG
              Piq3.setGeompyObject(Piq)
        if(typ == 'Droite'):
            if cas in (3,4):
              FondD,Piq=couperFondPiquagePosCas3Ou4(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondD = FondD
              Piq3.setGeompyObject(Piq)
            if cas == 2:
              FondD,Piq=couperFondPiquagePosCas2(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondD = FondD
              Piq3.setGeompyObject(Piq)
            if cas == 1:
              FondD,Piq=couperFondPiquagePosCas1(Piq3.geompyObject(),self._Corps,self._geompy)
              self._fondD = FondD
              Piq3.setGeompyObject(Piq)
        self._updateCorps()
        self._piquages.append(Piq3)
    def validAxialPiquage(self,Piq):
        return (Piq.Rposition()+Piq.Rpiquage) < self._Dvirole/2.
    def intersectWithAxis(self,Piq):
        if (Piq.Xp() < 0.):
            return Piq.RPosition() < Piq.RPiquage()
        else:
            return abs(Piq.Yp()) < Piq.RPiquage()
    def intersectWitRcare(self,Piq):
        return Piq.RPosition()+Piq.RPiquage() > 4.*self._Dvirole/9.
    def piquageAxialCase(self,Piq):
        if (self.intersectWithAxis(Piq) and self.intersectWitRcare(Piq)):
            return 1
        if (not self.intersectWithAxis(Piq) and self.intersectWitRcare(Piq)):
            return 2
        if (self.intersectWithAxis(Piq) and not self.intersectWitRcare(Piq)):
            return 3
        if (not self.intersectWithAxis(Piq) and not self.intersectWitRcare(Piq)):
            return 4
    def virole(self):
        return self._virole
    def fondG(self):
        return self._fondG
    def fondD(self):
        return self._fondD
    def pieds(self):
        return self._pieds
    def piquages(self):
        return self._piquages
    def groups(self):
        base=['Virole','FondG','FondD','Pieds']
        piqs = map(lambda x:x.name(),self._piquages)
        brids = map(lambda x:x.nameBride(),self._piquages)
        return base+piqs+brids
    def fabriquerBidon(self):
        comps= [self._virole,self._fondG,self._fondD,self._pieds]
        for piq in self._piquages:
            comps.append(piq.geompyObject())
        for piq in self._piquages:
            comps.append(piq.brideObject())
        return creerBidon(comps,self._geompy)
    def genererPointComm(self,nomFichier='bidonos.comm',pression=1.):
        fid=open(nomFichier,'w')
        fid.write(bidonCommPart1)
        msg="_F(GROUP_MA='Virole',EPAIS={0}),\n".format(self._eVirole)
        fid.write(msg)
        msg="\t _F(GROUP_MA=('FondG','FondD'),EPAIS={0}),\n".format(self._eFond)
        fid.write(msg)
        for piq in self._piquages:
             X=1.;Y=0.;Z=0.
             if(isinstance(piq,piquageVirole)):
                    X=0;Y=cos(piq.Alpha());Z=sin(piq.Alpha())
             msg="\t\t _F(GROUP_MA='{0}',EPAIS={1},VECTEUR=({2},{3},{4})),\n".format(piq.name(),piq.epaisseur(),X,Y,Z)
             fid.write(msg)
        for piq in self._piquages:
             X=0.;Y=1.;Z=0.
             if(isinstance(piq,piquageVirole)):
                    X=1.;Y=0.;Z=0.
             msg="\t\t _F(GROUP_MA='{0}',EPAIS={1},VECTEUR=({2},{3},{4})),\n".format(piq.nameBride(),piq.epaisseurBride(),X,Y,Z)
             fid.write(msg)
        fid.write('));')
        fid.write(bidonCommPart2)
        ls=['Virole','FondG','FondD']
        ls+=map(lambda x:x.name(),self._piquages)
        msg="\t\t_F(GROUP_MA=("
        for l in ls:
            msg+="'{0}',".format(l)
        msg+="),\nPRES={0}),);\n".format(pression)
        fid.write(msg)
        fid.write(bidonCommPart3)
        fid.close()
        
