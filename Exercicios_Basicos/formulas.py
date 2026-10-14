#MÓDULO DAS FUNÇÕES MATEMÁTICAS

def Euler(n):
    resultado = n*n - n + 41
    return resultado

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fibonacci(num):
    a = 0
    b = 1
    soma = 0
    contador = 0

    while a < num:
        soma = soma + a
        contador += 1
        proximo = a + b
        a = b
        b = proximo

    return contador, soma
