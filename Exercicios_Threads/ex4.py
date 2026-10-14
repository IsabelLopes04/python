import threading
import time
import random
from queue import Queue

# Fila compartilhada
fila = Queue(maxsize=5)

def produtor(q):
    for i in range(5):
        item = random.randint(1, 100)

        # Adiciona à fila (bloqueia se estiver cheia)
        q.put(item)

        print(f"Produzido: {item}")

        time.sleep(1)

    # Sinal de término para o consumidor
    q.put(None)

def consumidor(q):
    while True:
        # Retira da fila (bloqueia se estiver vazia)
        item = q.get()

        if item is None:
            q.task_done()
            break
        print(f"Consumido: {item}")

        time.sleep(1.5)

        q.task_done()
# Criando as threads
t_prod = threading.Thread(target=produtor, args=(fila,))
t_cons = threading.Thread(target=consumidor, args=(fila,))

# Iniciando as threads
t_prod.start()
t_cons.start()

# Esperando as threads terminarem
t_prod.join()
t_cons.join()

print("Processo finalizado!")