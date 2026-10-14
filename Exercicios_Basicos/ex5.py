# Use a fórmula de Euler n*n -n +41 para gerar números, sendo n=1 a 1000, quantos são primos?

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


contador = 0

for n in range(1,1000):
    num = n*n - n + 41
    if primo(num):
        contador += 1

print(f"A quantidade de números é: " ,contador)