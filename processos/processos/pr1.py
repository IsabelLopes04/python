import psutil

# Percentual de uso global da CPU (bloqueia por 1 segundo para medir)
print(f"Uso da CPU: {psutil.cpu_percent(interval=1.0)}%")

# Quantidade de núcleos físicos e lógicos
print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos lógicos: {psutil.cpu_count(logical=True)}")