import os
import random
import csv

with open("NomeHomens.txt", "r", encoding="utf-8") as arquivo:
    homens = arquivo.read().splitlines()

with open("NomeMulheres.txt", "r", encoding="utf-8") as arquivo:
    mulheres = arquivo.read().splitlines()

with open("Sobrenomes.txt", "r", encoding="utf-8") as arquivo:
    sobrenomes = arquivo.read().splitlines()

sexos = ["Masculino", "Feminino", "Não binário", "Não declarado"]

cidades = ["Caraguatatuba", "Ubatuba", "São Sebastião", "Ilhabela"]

with open("Clientes.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
    tabela = csv.writer(arquivo, delimiter=";")
    tabela.writerow(["CPF", "Nome", "Sexo", "Cidade", "Estado"])

    for cpf in os.listdir("../Exercicios_CPF"):
        caminho = "../Exercicios_CPF/" + cpf

        if os.path.isdir(caminho) and os.path.isdir(caminho + "/compras") and os.path.isdir(caminho + "/vendas"):
            sexo = random.choice(sexos)

            if sexo == "Masculino":
                nome = random.choice(homens)

            elif sexo == "Feminino":
                nome = random.choice(mulheres)
                
            else:
                todos = homens + mulheres
                nome = random.choice(todos)

            sobrenome = random.choice(sobrenomes)
            cidade = random.choice(cidades)

            nome_completo = nome + " " + sobrenome

            tabela.writerow([cpf, nome_completo, sexo, cidade, "SP"])

print("Arquivo Clientes.csv criado")