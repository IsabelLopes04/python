# Crie um programa que faca 500 threads que somam 10 a um valor e 
# 500 threads que subtraiam 10 de uma valor O valor final deve ser 1000

import threading
valor = 1000

def somar():
    global valor
    valor += 10

def diminuir():
    global valor
    valor -= 10

threads = []

for i in range(500):
    thread = threading.Thread(target=somar)
    threads.append(thread)
    thread.start()

for i in range(500):
    thread1 = threading.Thread(target=diminuir)
    threads.append(thread1)
    thread1.start()

for thread in threads:
    thread.join()

print("Valor final:", valor)

