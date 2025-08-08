from pathlib import Path
import shutil
import os


# CRIANDO AS PASTAS
nome_pastas = ['organizada', 'csv', 'html', 'json', 'pdf', 'py', 'txt', 'xlsx', 'backups']

def criando_pastas(nome_pasta_criada=''):
    pasta_atual = Path(__file__).parent
    if not os.path.isdir(pasta_atual):
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

def copiando_arquivos(pasta_específica= '',copiar_arquivos = ''):
    pasta_atual = Path(__file__).parent
    caminho_arquivo = pasta_atual /'arquivos_desafio'/ copiar_arquivos
    caminho_pasta_destino = pasta_atual / 'organizada'/ pasta_específica / copiar_arquivos
    shutil.copy2(caminho_arquivo, caminho_pasta_destino)
        

copiando_arquivos(pasta_específica= 'pdf', copiar_arquivos= 'vheeu.pdf')   
    

    

    


