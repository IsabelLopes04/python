import psutil
# Listar os 5 processos que mais consomem memória
processos = []
for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
    try:
        processos.append(proc.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Ordenar por uso de memória
processos_ordenados = sorted(processos, key=lambda x: x['memory_percent'], reverse=True)
for p in processos_ordenados[:5]:
    print(f"PID: {p['pid']} | Nome: {p['name']} | Uso de Memória: {p['memory_percent']:.2f}%")

# Exemplo: Como encerrar um processo pelo PID (com segurança)
# proc = psutil.Process(PID_AQUI)
# proc.terminate()