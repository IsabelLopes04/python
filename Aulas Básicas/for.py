lista = ["Alfredo", "Mario", "José", "Carolina", "Joana", "Luiza"]
for nome in lista:
    print(nome)
print("Range com 1 parâmetro") 

for i in range(2): 
    print(i)
print("Range com 2 parâmetros") 

for i in range(3,10): 
    print(i)

print("Exemplo break") 
for i in range(1,11): 
    if i % 5 == 0: 
        break 
    print(i)

print("Exemplo continue") 
for i in range(1,11): 
    if i % 5 == 0: 
        continue # Evitar usar break e continue, pois eles podem deixar o código confuso e dar bugs.
    print(i)
