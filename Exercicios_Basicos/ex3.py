# Crie uma função que calcule os números da sequencia de Fibonacci. 
# Quantos números de Fibonacci menores que 1.000.000 existem e qual a soma deles.

a = 0
b = 1
soma = 0
contador = 0

while a < 1000000:
    soma = soma + a
    contador += 1
    proximo = a + b
    a = b
    b = proximo

print("Quantidade:", contador)
print("Soma dos números:", soma)