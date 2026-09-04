def print_info(**kwargs): # kwargs é um dicionário que recebe os parâmetros passados para a função
    for parametro, valor in kwargs.items(): 
        print(parametro + " - " + str(valor))
print_info(nome="Felipe", idade=30, nacionalidade="Brasil")

def print_tudo_2_vezes(*args): 
    for parametro in args: print(parametro + "! " + parametro + "!")
print_tudo_2_vezes("Olá", "Python", "Felipe")

