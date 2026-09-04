#Exiba na tela os números menores que 1.000.000.000 que são divididos por 13, 23 e 41 ao mesmo tempo. Mostre também quantos números você achou.

contador = 1
while contador < 100000000:
    if((contador % 13 == 0) and (contador % 23 == 0) and (contador % 41 == 0)):
        print(contador)

    contador += 1

