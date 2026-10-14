import threading
import time

# Cria um objeto Lock
lock = threading.Lock()

contador = 0

def incrementar(nome_thread):
    global contador
    # Adquire o bloqueio manualmente
    lock.acquire()

    try:
        print(f"Thread {nome_thread} adquiriu o lock.")

        valor_atual = contador

        time.sleep(0.1)  # Simula um trabalho

        contador = valor_atual + 1

        print(f"Thread {nome_thread} atualizou o contador para {contador}")

    finally:
        # Garante que o lock será liberado mesmo se houver erro
        lock.release()

        print(f"Thread {nome_thread} liberou o lock.")

# Cria duas threads
t1 = threading.Thread(target=incrementar, args=("A",))
t2 = threading.Thread(target=incrementar, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Valor final do contador: {contador}")