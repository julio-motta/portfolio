
# Leitor de Arquivos em Python
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            print(f'O arquivo tem {len(linhas)} linhas.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')

# Exemplo de uso
# ler_arquivo('exemplo.txt')
