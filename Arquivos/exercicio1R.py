#utiluize random.sample para gerar 10 linhas com seis numeros (1 a 60) e salvar em um arquivo chamado 'numeros.txt'
import random

with open('numeros1.txt', 'w', encoding='utf-8') as arquivo:
    for _ in range(10):
        numeros = random.sample(range(1, 61), 6)
        arquivo.write(', '.join(map(str, numeros)) + '\n')

with open('numeros1.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())

# utilize range para gerar 10 linhas com seis numeros (1 a 60) e salvar em um arquivo chamado 'numeros2.txt'
with open('numeros2.txt', 'w', encoding='utf-8') as arquivo:    
    for i in range(10):
        numeros = [str(j) for j in range(i * 6 + 1, i * 6 + 7)]
        arquivo.write(', '.join(numeros) + '\n')
        
with open('numeros1.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())   