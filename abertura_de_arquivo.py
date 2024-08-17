import os

# Função que realiza a busca da palavra no arquivo
def busca_palavra(arquivo, palavra):
    with open(arquivo, 'r') as f:
        for i, linha in enumerate(f, 1):
            if palavra in linha:
                return i, linha
    return None

# Leitura do nome do arquivo e da palavra a ser buscada
arquivo = input("Digite o nome do arquivo: ")
palavra = input("Digite a palavra a ser buscada: ")

# Verificação se o arquivo existe
if not os.path.isfile(arquivo):
    print("Arquivo não encontrado.")
else:
    # Busca da palavra no arquivo
    resultado = busca_palavra(arquivo, palavra)
    if resultado:
        linha, conteudo = resultado
        print("Palavra encontrada na linha {}:".format(linha))
        print(conteudo)
    else:
        print("Palavra não encontrada.")
