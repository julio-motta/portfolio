
# Script: leitor_arquivos.py
# Função: Ler um arquivo .txt e contar linhas

arquivo = input("Digite o nome do arquivo .txt: ")

try:
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        print(f"O arquivo tem {len(linhas)} linhas.")
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
