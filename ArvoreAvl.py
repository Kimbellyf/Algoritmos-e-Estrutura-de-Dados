class NoArvore:
    def __init__(self, Dado):
        self._Dado = Dado
        self._noEsq = None
        self._noDir = None
        self._Pai = None
    
    def getDado(self):
        return self._Dado
    def setDado(self, Dado):
        self._Dado = Dado
    def getnoDir(self):
        return self._noDir
    def setnoDir(self, novoNo):
        self._noDir = novoNo
    def getnoEsq(self):
        return self._noEsq
    def setnoEsq(self, novoNo):
        self._noEsq = novoNo

    def getPai(self):
        return self._Pai
    def setPai(self, novoNo):
        self._Pai = novoNo
    
        
class ArvBin:
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, novoNo):
        self._raiz = novoNo
    
    def Ordem(self, raiz, li):
        if raiz != None:
            self.Ordem(raiz.getnoEsq(), li)
            li.append(raiz.getDado())
            self.Ordem(raiz.getnoDir(), li)
            
    def PreOrdem(self, raiz, li):
        if raiz != None:
            li.append(raiz.getDado())
            self.PreOrdem(raiz.getnoEsq(), li)
            self.PreOrdem(raiz.getnoDir(), li)
            
    def PosOrdem(self, raiz, li):
        if raiz != None:
            self.PosOrdem(raiz.getnoEsq(), li)
            self.PosOrdem(raiz.getnoDir(), li)
            li.append(raiz.getDado())                
    
    def pesquisar(self, Dado):
        raiz = self._raiz
        while raiz != None and Dado != raiz.getDado():
            if Dado < raiz.getDado():
                raiz = raiz.getnoEsq()
            else:
                raiz = raiz.getnoDir()
        return raiz
    
    def min(self, raiz):
        while raiz.getnoEsq() != None:
            raiz = raiz.getnoEsq()
        return raiz
    
    def max(self, raiz):
        while raiz.getnoDir() != None:
            raiz = raiz.getnoDir()
        return raiz

    def sucessor(self, no):
        if no.getnoDir() != None:
            return self.min(no.getnoDir())
        y = no.getPai()
        while y != None and no == y.getnoDir():
            no = y 
            y = y.getPai()
        return y
    
    def antecessor(self, no):
        if no.getnoEsq() != None:
            return self.max(no.getnoEsq())
        y = no.getPai()
        while y != None and no == y.getnoEsq():
            no = y 
            y = y.getPai()
        return y
    
    def add(self, Dado):
        no = NoArvore(Dado)
        y = None
        raiz = self.getRaiz()
        while raiz != None:
            y = raiz
            if no.getDado() < raiz.getDado():
                raiz = raiz.getnoEsq()
            else:
                raiz = raiz.getnoDir()
        no.setPai(y)
        if y == None:
            self.setRaiz(no)
        elif no.getDado() < y.getDado():
            y.setnoEsq(no)
        else:
            y.setnoDir(no)
        return no, y
                
    def remover(self, Dado):
        no = self.pesquisar(Dado)
        if no.getnoEsq() == None or no.getnoDir() == None:
            y = no
        else:
            y = self.sucessor(no)
        if y.getnoEsq() != None:
            x = y.getnoEsq()
        else:
            x = y.getnoDir()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getnoEsq():
                y.getPai().setnoEsq(x)
            else:
                y.getPai().setnoDir(x)
        if y != no:
            no.setDado(y.getDado())
        return y.getDado(), y.getPai()

class noAvl(NoArvore):
    def __init__(self, Dado):
        super(noAvl, self).__init__(Dado)
        self._altura = -1

class ArvoreAvl(ArvBin):

    def NoAlt(self, no):
        if no == None:
            return -1
        h1 = self.NoAlt(no.getnoEsq())
        h2 = self.NoAlt(no.getnoDir())
        return 1 + max(h1, h2)
    
    def addAvl(self, Dado):
        no, pai = super(ArvoreAvl, self).add(Dado)
        while pai != None:
            if self.balancear(pai.getDado()) == True:
                break
            else:
                pai = pai.getPai()
                    
    def removerAvl(self, Dado):
        no, pai = super(ArvoreAvl, self).remover(Dado)
        self.balancear(pai.getDado())
        
    def balancear(self, no):
        x = self.fatorBalanc(self.pesquisar(no))
        if x >= -1 and x <= 1:
            return False
        if x > 1:
            if self.fatorBalanc(self.pesquisar(no).getnoDir()) < 0:
                self.giroDir(self.pesquisar(no).getnoDir())
                self.giroEsq(self.pesquisar(no))
            else:
                self.giroEsq(self.pesquisar(no))
            return True
        else:
            if self.fatorBalanc(self.pesquisar(no).getnoEsq()) > 0:
                self.giroEsq(self.pesquisar(no).getnoEsq())
                self.giroDir(self.pesquisar(no))
            else:
                self.giroDir(self.pesquisar(no))
            return True

    def fatorBalanc(self, no):
        altEsq = self.NoAlt(no.getnoEsq())
        altDir = self.NoAlt(no.getnoDir())
        return altDir - altEsq

    def giroEsq(self, x):
        y = x.getnoDir()
        x.setnoDir(y.getnoEsq())
        if y.getnoEsq() != None:
            y.getnoEsq().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        elif x == x.getPai().getnoEsq():
            x.getPai().setnoEsq(y)
        else:
            x.getPai().setnoDir(y)
        y.setnoEsq(x)
        x.setPai(y)
        
    def NivelNodo(self,num):
        aux=self.getRaiz()
        nivel=1

        while True:
            if aux==None:
                nivel=-1
                break
            elif aux.getDado()==num:
                break

            if (num<aux.getDado()):
                aux=aux.getnoEsq()
            else:
                aux=aux.getnoDir()

            nivel+=1
        return nivel

    def giroDir(self, x):
        y = x.getnoEsq()
        x.setnoEsq(y.getnoDir())
        if y.getnoDir() != None:
            y.getnoDir().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        elif x == x.getPai().getnoDir():
            x.getPai().setnoDir(y)
        else:
            x.getPai().setnoEsq(y)
        y.setnoDir(x)
        x.setPai(y)

    def giroDuploEsquerdo(self, no):
        self.giroDir(no)
        self.giroEsq(no)

    def giroDuploDireito(self, no):
        self.giroEsq(no)
        self.giroDir(no)
        
