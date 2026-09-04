# Conte quantos números primos menores que 1.000.000.000 existem.

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador = 0
for x in range (1,1000000000):
    if primo(x):
        contador += 1

print(f" A quantidadde de números é: " ,contador)