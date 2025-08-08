from pathlib import Path
import shutil
import os

'''
#copiando arquivo com copyfile
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino 2' / 'texto.txt'
shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)
'''

'''
#copiando arquivo com copy
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino 2'
shutil.copy(caminho_arquivo, caminho_pasta_destino)
'''

'''
#copiando arquivo com copy2
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino 3'
shutil.copy2(caminho_arquivo, caminho_pasta_destino)
'''
'''
#movendo arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino 3' / 'texto.txt'

shutil.move(caminho_arquivo, caminho_pasta_destino)
'''
#deletando arquivos
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino 2'
#shutil.copy(caminho_arquivo, caminho_pasta_destino)

if caminho_arquivo.exists():
    os.remove(caminho_arquivo)