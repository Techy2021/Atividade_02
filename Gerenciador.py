import os
import shutil

def listar_documentos_por_tipo_ano(pasta_base):
    documentos = {}
    for raiz, _, arquivos in os.walk(pasta_base):
        for arquivo in arquivos:
            tipo = arquivo.split('.')[-1].lower()
            ano = os.path.basename(raiz)
            documentos.setdefault(ano, {}).setdefault(tipo, []).append(arquivo)
    return documentos

def adicionar_documento(origem, destino):
    shutil.copy(origem, destino)

def renomear_documento(caminho_atual, novo_nome):
    pasta = os.path.dirname(caminho_atual)
    os.rename(caminho_atual, os.path.join(pasta, novo_nome))

def remover_documento(caminho):
    os.remove(caminho)
