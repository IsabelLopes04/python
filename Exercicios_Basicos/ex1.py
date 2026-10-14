#Crie uma função que determine se um número é primo ou não. Retorne True ou False.
 
def primo(n): 
    if n <= 1:
        return False
    
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True