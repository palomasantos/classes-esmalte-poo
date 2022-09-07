class Esmalte:
    def __init__(self, nome, acabamento,marca):
        self.nome = nome
        self.acabamento = acabamento
        self.marca = marca
        
    def name(self):
        return f'Seu esmalte se chama {self.nome}'
    
    def texture(self):
        return f'Ele tem o acabamento{self.acabamento}'

class Vencimento(Esmalte):
    def __init__(self, validade, profissional, nome, acabamento,marca):
        self.validade = validade
        self.profissional = profissional
        super().__init__(nome,acabamento,marca)
   
    def __validity(self):
        return f'Seu esmalte vence em: {self.validade}'
      
    def permission(self):
        if self.profissional == 'Amanda':
              return self.__validity()   
    
cliente1 = Vencimento("12/25",'Amanda','Renda','Cremoso','Risque')

print(cliente1.permission(),'\n',cliente1.name())