# Conte quantos números primos menores que 1.000.000.000 existem.

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

contador = 0
for n in range (1,1000000000):
    if primo(n):
        contador += 1

print(f" A quantidadde de números é: " ,contador)