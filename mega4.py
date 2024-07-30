from collections import defaultdict

# Função para ler o arquivo results.txt e contar a frequência dos números
def ler_resultados(arquivo):
    frequencia = defaultdict(int)
    with open(arquivo, 'r') as file:
        for linha in file:
            numeros = linha.strip().split(',')
            for numero in numeros:
                frequencia[int(numero)] += 1
    return frequencia

# Função para calcular a probabilidade de cada número ser sorteado
def calcular_probabilidade(frequencia):
    total_numeros = sum(frequencia.values())
    probabilidades = {numero: frequencia[numero] / total_numeros for numero in range(1, 61)}
    return probabilidades

# Função para retornar a sequência com maior probabilidade de ser sorteada
def sequencia_probavel(probabilidades, sequencias_anteriores):
    numeros_utilizados = set()
    sequencia = []

    for _ in range(6):
        max_probabilidade = 0
        proximo_numero = None
        for numero, probabilidade in probabilidades.items():
            if numero not in numeros_utilizados and probabilidade > max_probabilidade:
                max_probabilidade = probabilidade
                proximo_numero = numero
        sequencia.append(proximo_numero)
        numeros_utilizados.add(proximo_numero)

    return sequencia

# Ler resultados do arquivo e calcular probabilidades
frequencia = ler_resultados("results.txt")
probabilidades = calcular_probabilidade(frequencia)

# Gerar sequência provável
sequencia_provavel = sequencia_probavel(probabilidades, [])

print("Sequência provável:", sequencia_provavel)

