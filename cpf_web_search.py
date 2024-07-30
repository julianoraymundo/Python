import requests
from bs4 import BeautifulSoup

# Solicita ao usuário para inserir seu nome e CPF
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")

# Realiza a busca por informações na internet
results = []
url1 = f"https://www.exemplo.com/pesquisa?q={nome}"
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')
results.append({'site': url1, 'informacoes': soup1})

url2 = f"https://www.exemplo.com/pesquisa?q={cpf}"
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
results.append({'site': url2, 'informacoes': soup2})

# Organiza os resultados em uma lista
lista_resultados = []
for result in results:
    if 'informacoes' in result['informacoes']:
        lista_resultados.append({'site': result['site'], 'informacoes': result['informacoes']['informacoes']})

# Exibe os resultados em tela
print(lista_resultados)

# Exporta os resultados para um arquivo
with open('resultados.txt', 'w') as f:
    for resultado in lista_resultados:
        f.write(f"{resultado['site']}: {resultado['informacoes']}\n")
