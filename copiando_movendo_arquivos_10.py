from pathlib import Path
import shutil
import os

'''
#criando pasta
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino 1'
caminho_pasta_destino.mkdir(exist_ok=True) # mkdir --> fazer diretório
'''

'''
#criando pasta com todas as pastas anteriores necessárias
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino 5'
caminho_pasta_destino.mkdir(exist_ok=True)
caminho_pasta_destino = pasta_atual / 'destino 5' / 'destino 5.1'
caminho_pasta_destino.mkdir(exist_ok=True)
'''
'''
#ou usar outro método para criar as duas pastas juntas
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino 5' / 'destino 5.1'
caminho_pasta_destino.mkdir(parents=True)
'''                       
'''
#copiando pastas
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual/'destino 5', pasta_atual/ ' destino 1' / 'destino 5')
'''

'''
#deletando pastas vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino 5' / 'destino 5.1'
pasta_remover.rmdir()
'''
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino 1' 
pasta_remover.rmdir() # só deleta pastas vazias
'''
'''
#deletando pastas com conteúdo
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino 1' 
shutil.rmtree(pasta_remover)
'''