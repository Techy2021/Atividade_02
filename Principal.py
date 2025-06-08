# Programa de interface com o usuário

from Gerenciador import *  #correção do nome "Gerenciador"
import os

def menu():
    while True:
        print("\n[1] Listar documentos\n[2] Adicionar\n[3] Renomear\n[4] Remover\n[5] Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            resultado = listar_documentos_por_tipo_ano("documentos")
            for ano, tipos in resultado.items():
                print(f"\nAno: {ano}")
                for tipo, arquivos in tipos.items():
                    print(f"  {tipo}: {arquivos}")
        elif opcao == "2":
            origem = input("Caminho do arquivo a adicionar: ")
            destino = input("Caminho de destino (ex: documentos/2025): ")
            adicionar_documento(origem, destino)
        elif opcao == "3":
            caminho = input("Caminho completo do arquivo: ")
            novo = input("Novo nome (com extensão): ")
            renomear_documento(caminho, novo)
        elif opcao == "4":
            caminho = input("Caminho completo do arquivo: ")
            remover_documento(caminho)
        elif opcao == "5":
            break

menu()
