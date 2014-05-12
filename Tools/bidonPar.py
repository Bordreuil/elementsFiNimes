from bidonChar import * 

availablePiquageType = ['Gauche','Droite']

class piquageVirole:
    def __init__(self,nom,Hpiquage,Dpiquage,Alpha,Position,Dbride):
        self._nom      = nom
        self._hpiquage = Hpiquage
        self._dpiquage = Dpiquage
        self._alpha    = Alpha
        self._position = Position
        self._dbride   = Dbride
        self.buildGeompyObject()
    def name(self):
        return self._nom
    def buildGeompyObject(self):
        self._obj = creerPiquageVirole(self._position,self._hpiquage,self._alpha,self._dpiquage,self._dbride)
    def geompyObject(self):
        return self._obj
    def setGeompyObject(self,obj):
        self._obj = obj
    def onPositiveSide(self):
        return self._position > 0.
class piquageFond:
    def __init__(self,nom,Type,Hauteur,Rpiquage,Alpha,Dpiquage,Dbride):
        self._nom      = nom
        if Type in availablePiquageType:
            self._type     = Type
        else:
            msg = 'Attention le type de piquage doit etre dans la liste:'+availablePiquageType
            print msg
            self._type = availablePiquageType[0]
        self._hauteur  = Hauteur
        self._rpiquage = Rpiquage
        self._alpha    = Alpha
        self._dpiquage = Dpiquage
        self._Dbride   = Dbride
    def name(self):
        return self._nom
    def 
class bidonFondGRC:
    def __init__(self,Dvirole      = 500.,
                      Lvirole      = 1200.,
                      PositionPieds= 1280.,
                      LargeurPieds = 900.,
                      largeurPieds = 300.,
                      HauteurPieds = 800.):

        self._Dvirole       = Dvirole
        self._Lvirole       = Lvirole
        self._PositionPieds = PositionPieds
        self._LargeurPieds  = LargeurPieds
        self._largeurPieds  = largeurPieds
        self._HauteurPieds  = HauteurPieds
 
        OX                  = geompy.MakeVectorDXDYDZ(1, 0, 0)
        self._Axe           = OX
        Virole,FondG,FondD  = creerViroleEtDeuxGRC(Lvirole,Dvirole,OX)
        Pied1,Pied2         = creerPiedsEnU(PositionPieds,
                                            largeurPieds,
                                            LargeurPieds,
                                            HauteurPieds,
                                            Dvirole)

       
        Corps = geompy.MakeCompound([Virole,
                                             FondG,
                                             FondD])
        Virole,Pieds  = couperPiedEtBidon(Pied1,Pied2,Corps)
        self._virole  = Virole
        self._fondG   = FondG
        self._fondD   = FondD 
        self._pieds   = Pieds
        self._piquages = []
        self._updateCorps()

    def _updateCorps(self):
         self._Corps  = geompy.MakeCompound([self._virole,
                                             self._fondG,
                                             self._fondD])
    def ajouterPiquageVirole(self,nom,Hpiquage,Dpiquage,Alpha,Position,Dbride):
        Piq2          = piquageVirole(nom,Hpiquage,Dpiquage,Alpha,Position,Dbride)

        if Piq2.onPositiveSide():
            Virole,Piq    = couperVirolePiquagePos(Piq2.geompyObject(),self._Corps)
            self._virole  = Virole
            Piq2.setGeompyObject(Piq)
        else:
            Virole,Piq    = couperVirolePiquageNeg(Piq2.geompyObject(),self._Corps)
            self._virole  = Virole
            Piq2.setGeompyObject(Piq)           

        self._updateCorps()
        self._piquages.append(Piq2)
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
        return base+piqs
    def fabriquerBidon(self):
        comps= [self._virole,self._fondG,self._fondD,self._pieds]
        for piq in self._piquages:
            comps.append(piq.geompyObject())
        return creerBidon(comps)
