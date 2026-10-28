# Crie um programa python que gere dez cpfs válidos
# Crie uma pasta para cada cpf cujo nome é o cpf
# Dentro de cada pasta de cpf crie uma pasta para compras e outra para vendas

import os
import random

def gerar_cpf():
    cpf = ""

    for i in range(9):
        numero = random.randint(0, 9)
        cpf = cpf + str(numero)

    soma = 0
    peso = 10

    for i in range(9):
        soma = soma + int(cpf[i]) * peso
        peso = peso - 1

    resto = soma % 11

    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto

    cpf = cpf + str(digito)

    soma = 0
    peso = 11

    for i in range(10):
        soma = soma + int(cpf[i]) * peso
        peso = peso - 1

    resto = soma % 11

    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto

    cpf = cpf + str(digito)

    return cpf


for i in range(10):
    cpf = gerar_cpf()

    os.mkdir(cpf)
    os.mkdir(cpf + "/compras")
    os.mkdir(cpf + "/vendas")

    print("CPF criado:", cpf)