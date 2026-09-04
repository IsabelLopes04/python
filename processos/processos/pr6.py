import subprocess

try:
    # O argumento check=True dispara uma exceção se o comando falhar
    resultado = subprocess.run(["dir", ""], capture_output=True, text=True, check=True)
    print("Arquivos encontrados:\n", resultado.stdout)
except subprocess.CalledProcessError as e:
    print("O comando falhou com o código:", e.returncode)
