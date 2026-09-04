class Usuario: 
    def __init__(self, nome, email):
        #palavras reservadas, self é uma referência para ele mesmo, é uma convenção do python, mas poderia ser qualquer nome, mas é recomendado usar self                                                                              
        # primeiro parâmetro é sempre self, que é uma referência para o próprio objeto, e os outros parâmetros são os atributos do objeto
        self.nome = nome 
        self.email = email       
    def diga_ola(self): 
        print("Olá, meu nome é %s e meu email é %s" % (self.nome, self.email))
        
usuario1 = Usuario(nome="Felipe", email="contato@felipegalvao.com.br")
usuario1.diga_ola() 
print(usuario1.nome)
usuario1.nome = "Felipe Galvão"
print(usuario1.nome)

