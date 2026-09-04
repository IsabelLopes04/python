contador = 0
while contador < 5: 
    print(contador) 
    contador = contador + 1


    while True: 
        nome = input("Digite seu nome ou sair para terminar o programa: ") 
        if nome == "sair": 
            break 
        else: 
            print("Olá, %s" % nome)
