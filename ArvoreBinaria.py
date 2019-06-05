class No:
    def __init__(self,idNoh):
        self.idNoh=idNoh
        self.Pai=None
        self.FilhoDir=None
        self.FilhoEsq=None

    def getidNoh(self):
        return self.idNoh
    
    def setidNoh(self,novo):
        self.idNoh=novo

    def getPai(self):
        return self.Pai

    def setPai(self,novo):
        self.Pai=novo

    def getFilhoDir(self):
        return self.FilhoDir

    def setFilhoDir(self,novo):
        self.FilhoDir=novo

    def getFilhoEsq(self):
        return self.FilhoEsq

    def setFilhoEsq(self,novo):
        self.FilhoEsq=novo

    def __str__(self):
        return str("No: " +str(self.getidNoh()))



class Tree:
    def __init__(self):
        self.Raiz=None

    def getRaiz(self):
        return self.Raiz.getidNoh()

    def setRaiz(self,novo):
        self.Raiz=novo

    def inserir(self,idNoh):
        novoNoh=No(idNoh)
        if self.Raiz==None:
            self.Raiz=novoNoh
        else:
            NohAtual=self.Raiz
            while True:
                if idNoh<NohAtual.getidNoh():
                    if NohAtual.getFilhoEsq()==None:
                        NohAtual.setFilhoEsq(novoNoh)
                        novoNoh.setPai(NohAtual)
                        break
                    NohAtual=NohAtual.getFilhoEsq()
                else:
                    if NohAtual.getFilhoDir()==None:
                        NohAtual.setFilhoDir(novoNoh)
                        novoNoh.setPai(NohAtual)
                        break
                    NohAtual=NohAtual.getFilhoDir()
                    
    def pesquisar(self,idDoNohPesq):
        NohAtual=self.Raiz
        while NohAtual!=None:
            if NohAtual==None:
                return None
            if (NohAtual.getidNoh())!=idDoNohPesq:
                if idDoNohPesq<NohAtual.getidNoh():
                    NohAtual=NohAtual.getFilhoEsq()
                else:
                    NohAtual=NohAtual.getFilhoDir()
            else:
                break
        return NohAtual

    def PreOrdem(self,Noh,printar):
        self.printarPreOrdem1=printar
        if self.Raiz==None:
            self.printarPreOrdem1+="0"+" "
        else:
            if Noh!=None:
                self.printarPreOrdem1+=str(Noh.getidNoh())+" "
                self.PreOrdem(Noh.getFilhoEsq(),self.printarPreOrdem1)
                self.PreOrdem(Noh.getFilhoDir(),self.printarPreOrdem1)

    def printarPreOrdem(self):
        self.PreOrdem(self.Raiz,"")
        return( self.printarPreOrdem1[:-1])

    def Ordem(self,Noh,printar):
        self.printarOrdem1=printar
        if self.Raiz==None:
            self.printarOrdem1+="0"+" "
        else:
            if Noh !=None:
                self.Ordem(Noh.getFilhoEsq(),self.printarOrdem1)
                self.printarOrdem1+=str(Noh.getidNoh())+" "
                self.Ordem(Noh.getFilhoDir(),self.printarOrdem1)
                
    def printarOrdem(self):
        self.Ordem(self.Raiz,"")
        return(self.printarOrdem1[:-1])

    def PosOrdem(self,Noh,printar):
        self.printarPosOrdem1=printar
        if self.Raiz==None:
            self.printarPosOrdem1+="0"+" "
            
        else:
            if Noh!=None:
                self.PosOrdem(Noh.getFilhoEsq(),self.printarPosOrdem1)
                self.PosOrdem(Noh.getFilhoDir(),self.printarPosOrdem1)
                self.printarPosOrdem1+=str(Noh.getidNoh())+" "

    def printarPosOrdem(self):
        self.PosOrdem(self.Raiz,"")
        return(self.printarPosOrdem1[:-1])


    def minimo(self,u):
        u=u
        while u.getFilhoEsq()!=None:
            u=u.getFilhoEsq()
        return u
    
    def maximo(self,u):
        u=u
        while u.getFilhoDir()!=None:
            u=u.getFilhoDir()
        return u
    
    def c(self,idNoh):
        Noh=self.pesquisar(idNoh)
        #print(Noh)
        if Noh==None:
            return("0")
        Pred=self.predecessorNovo(Noh)
        return Pred

    def sucessorProf(self,no):
        x=no
        if no.getFilhoDir()!=None:
            return self.minimo(no.getFilhoDir())
        y=no.getPai()
        while y!=None and x!=y.getFilhoDir():
            x=y
            y=x.getPai()
        return y

    def predecessorProf(self,no):
        x=no
        if no.getFilhoEsq()!=None:
            return self.maximo(no.getFilhoEsq())
        if no.getPai().getidNoh()>no.getidNoh():
            return 0
        '''while y!=None and x!=y.getFilhoEsq():
            x=y
            y=x.getPai()'''
        return "2"

    def predecessorNovo(self,no):
        x=no
        if no.getFilhoEsq()!=None:
            return self.maximo(no.getFilhoEsq())


        PaideX=x.getPai()
        if PaideX==None:
            return "0"
        elif x==PaideX.getFilhoDir():
            return PaideX.getidNoh()
        else:
            while x==PaideX.getFilhoEsq():
                x= PaideX
                PaideX=x.getPai()
                if PaideX==None:
                    return "0"

            return PaideX.getidNoh()
    def SucessorNovo(self,no):
        x=no
        if no.getFilhoDir()!=None:
            return self.minimo(no.getFilhoDir())


        PaideX=x.getPai()
        if PaideX==None:
            return "0"
        elif x==PaideX.getFilhoEsq():
            return PaideX.getidNoh()
        else:
            while x==PaideX.getFilhoDir():
                x= PaideX
                PaideX=x.getPai()
                if PaideX==None:
                    return "0"

            return PaideX.getidNoh()

    def remover(self,idNoh):
        x=self.pesquisar(idNoh)
        if x==None:
            pe=0
            #print("0")
        else:
            if x.getFilhoEsq()==None or x.getFilhoDir()==None:
                y=x
            else:
                y=self.SucessorNovo(x)
                #print(h)

                
            if y.getFilhoEsq()!=None:
                z=y.getFilhoEsq()
            else:
                z=y.getFilhoDir()
                
            if z!=None:
                z.setPai(y.getPai())

                
            if y.getPai()==None:
                self.Raiz=z
            else:
                if y==y.getPai().getFilhoEsq():
                    y.getPai().setFilhoEsq(z)
                else:
                    y.getPai().setFilhoDir(z)
            if y!=x:
                x.setidNoh(y.getidNoh())