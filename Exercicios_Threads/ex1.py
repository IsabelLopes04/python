import threading
import random

def gerar_cpf():
    cpf = [random.randint(0, 9) for i in range(9)]

    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)

    digito1 = (soma * 10 % 11) % 10
    cpf.append(digito1)

    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)

    digito2 = (soma * 10 % 11) % 10
    cpf.append(digito2)

    return ''.join(map(str, cpf))


def thread_function(nome, lista):
    cpf = gerar_cpf()
    lista[nome] = cpf
    print("Thread", nome, "gerou:", cpf)


if __name__ == "__main__":

    cpfs = [None] * 30
    threads = []

    for i in range(30):
        print("Criando thread", i)

        thread = threading.Thread(
            target=thread_function,
            args=(i, cpfs)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nCPFs gerados:")

    for cpf in cpfs:
        print(cpf)