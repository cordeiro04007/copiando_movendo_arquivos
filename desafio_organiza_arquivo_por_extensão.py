from pathlib import Path
import shutil
import os
import datetime



# CRIANDO AS PASTAS
nome_pastas = ['organizada', 'csv', 'html', 'json', 'pdf', 'py', 'txt', 'xlsx', 'backups']

def criando_pastas(nome_pasta_criada=''):
    pasta_atual = Path(__file__).parent
    if not os.path.isdir(pasta_atual / 'organizada'):
        caminho_pasta_destino = pasta_atual / nome_pasta_criada
        caminho_pasta_destino.mkdir(exist_ok=True)

################################################################

# MOVENDO AS PASTAS PARA A PASTA ORGANIZADA

def movendo_pastas (mover_pasta = ''):
    pasta_atual = Path(__file__).parent
    caminho_pasta = pasta_atual / mover_pasta
    caminho_pasta_destino = pasta_atual / 'organizada' /  mover_pasta
    if os.path.exists(caminho_pasta):
        if not os.path.isdir(caminho_pasta_destino):
            shutil.move(caminho_pasta, caminho_pasta_destino)

movendo_pastas(mover_pasta='csv')

for pasta in nome_pastas:
    criando_pastas(nome_pasta_criada= pasta)

################################################################

# COPIANDO OS ARQUIVOS PARA AS PASTAS ESPECÍFICAS

def copiando_arquivos():
    pasta_atual = Path(__file__).parent
    pasta_organizada = pasta_atual / 'organizada'
    pasta_a_organizar = pasta_atual / 'arquivos_desafio'
    #pasta_backup = pasta_atual / 'backups'
    for arquivo in pasta_a_organizar.glob('**/*'):
        if arquivo.is_file():
            pasta_organizada_c_extensão = pasta_organizada / arquivo.suffix.replace('.', '')
            if not pasta_organizada_c_extensão.exists():
                pasta_organizada_c_extensão.mkdir()
            shutil.copy(arquivo, pasta_organizada_c_extensão)
                                        
copiando_arquivos()   
    

    

    


