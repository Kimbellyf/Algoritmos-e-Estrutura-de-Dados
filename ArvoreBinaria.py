
class No:
    def __init__(self,dado):
        self._dado=dado
        self._Ant=None
        self._Prox=None

    def getDado(self):
        return self._dado

    def setDado(self,novodado):
        self._dado=novodado

    def getAnt(self):
        return self._Ant

    def setAnt(self,novoAnt):
        self._Ant=novoAnt

    def getProx(self):
        return self._Prox

    def setProx(self,novoDepois):
        self._Prox=novoDepois


class Lista:
    def __init__(self,inicio=None,fim=None):
        self._inicio=inicio
        self._fim=fim

    def Vazio(self):
        return self._inicio is None

    def insereInicio(self,dado):
        novoNoh=No(dado)
        if self.Vazio():
          self._inicio=self._fim=novoNoh
        else:
          novoNoh.setProx(self._inicio)
          self._inicio=novoNoh

    def insereFim(self,dado):
      novoNoh=No(dado)
      if self.Vazio():
        self._fim=self._inicio=novoNoh
      else:
        self._fim.setProx(novoNoh)
        self._fim=novoNoh

    def removeInicio(self):
        if self.Vazio():
            raise IndexError ("OPA")
        NohInicio=self._inicio.getDado()
        if self._inicio is self._fim:
            self._inicio=self._fim=None
        else:
            self._inicio=self._inicio.getProx()
        

    def removeFim(self):
        if self.Vazio():
            raise IndexError ("0")
        NohFim=self._fim.getDado()
        if self._fim is self._inicio:
            self._fim=self._inicio=None
        else: 
            NohAtual=self._inicio
            while NohAtual.getProx() is not self._fim:
              NohAtual=NohAtual.getProx()
            NohAtual.setProx(None)
            self._fim=NohAtual
            
        return NohFim

    def __str__(self):
        if self.Vazio():
            return "0"
        NohAtual=self._inicio
        string=""
        while NohAtual is not None:
          string+=str(NohAtual.getDado())+" "
          NohAtual=NohAtual.getProx()
        
        return string
        
    def primPosi(self):
        if self.Vazio():
            return "0"
        else:
            NohAtual=self._inicio
            stringw=str(NohAtual.getDado())
            return stringw

    def pesquisar(self,dado):
        if self.Vazio():
            return "O dado nao esta na lista pq ela ta vazia"
        else:
            NohAtual=self._inicio
            while NohAtual is not None:
                if NohAtual.getDado()==dado:
                    return "encontrei"
                else:
                    NohAtual=NohAtual.getProx()

