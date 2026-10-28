from pathlib import Path

# Definindo o caminho da nova pasta
caminho_pasta_destino = Path('destino4')

# Criando a pasta
caminho_pasta_destino.mkdir()

caminho_pasta_destino = Path('destino5/destino51')
caminho_pasta_destino.mkdir(parents=True)

import shutil

# Definindo o caminho da pasta original e da pasta de destino
pasta_original = Path('destino4')
pasta_destino = Path('destino1/destino4')

# Copiando a pasta
shutil.copytree(pasta_original, pasta_destino, dirs_exist_ok=True)