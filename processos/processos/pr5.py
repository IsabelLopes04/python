import psutil
disco = psutil.disk_usage('/')
print(f"Disco Total: {disco.total / (1024**3):.2f} GB")
print(f"Disco Livre: {disco.free / (1024**3):.2f} GB")
print(f"Percentual de uso: {disco.percent}%")
