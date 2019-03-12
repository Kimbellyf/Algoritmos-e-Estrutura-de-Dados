
class No:
    def __init__(self,idNo,ListaDados):
        self.idNo=idNo
        self.ListaDados=ListaDados
 
    def getIdNo(self):
        return self.idNo

    def setIdNo(self,novoId):
        self.idNo=novoId
        
    def getListaDados(self):
        return self.ListaDados

    def setListaDados(self,novaLista):
        self.ListaDados=novaLista

class TabelaHash:
    def __init__(self,funcao,N):
        self.funcao=funcao
        self.Tabela=[]
        for i in range(N):
            self.Tabela.append([])
        
    def Inserir(self,no):
        id_no=no.getIdNo()
        Dad=no.getListaDados()
        Pos=self.funcao(id_no)
        self.Tabela[Pos].append(Dad)

    def imprime(self):
        return self.Tabela

    def Deletar(self,IDNoh):
        Posi=self.funcao(IDNoh)
        if Daw!="None" and Daw!=[]:
            self.Tabela[Posi]=[]
        else:
            return ""

    def imprimeDados(self,IDNoh):
        Posi=self.funcao(IDNoh)
        Daw=self.Tabela[Posi][0]

        if Daw!="None" and Daw!=[]:
            return Daw
        else:
            return ""

    
    def Atualiza(self,IDNoh,ListaNova):
        Posi=self.funcao(IDNoh)
        self.Tabela[Posi]=[ListaNova]
        
  
