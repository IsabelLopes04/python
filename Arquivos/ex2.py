# cria (ou sobrescreve) o arquivo
with open('notas.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Olá, arquivo 4!\n')   

# Olá, arquivo!
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())             

# ler linhas específicas do arquivo
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    primeira = arquivo.readline()
    segunda = arquivo.readline()

print(repr(primeira))
print(repr(segunda))

## W - write
## R - read 
## A - append
## X - create new file 