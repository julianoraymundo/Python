import itertools

def gerar_proxima_sequencia(arquivo_resultados):
  """
  Gera a próxima sequência de números para sorteio.

  Argumentos:
    arquivo_resultados: Caminho para o arquivo `results.txt`.

  Retorno:
    Sequência de 6 números com alta probabilidade de ser a próxima a ser sorteada.
  """

  # Leitura do arquivo results.txt
  with open(arquivo_resultados, "r") as f:
    sequencias = [linha.strip().split(",") for linha in f]

  # Criação de um conjunto com todos os números sorteados
  numeros_sorteados = set()
  for sequencia in sequencias:
    numeros_sorteados.update(sequencia)

  # Criação de um conjunto com os números possíveis para a próxima sequência
  numeros_possiveis = set(range(1, 61)) - numeros_sorteados

  # Verificação de combinações
  combinacoes = itertools.combinations(numeros_possiveis, 6)
  sequencias_validas = []
  for combinacao in combinacoes:
    if combinacao not in sequencias:
      sequencias_validas.append(combinacao)

  # Retorno da sequência com maior probabilidade
  ultima_sequencia = sequencias[-1]
  soma_ultima_sequencia = sum(int(numero) for numero in ultima_sequencia)
  sequencia_escolhida = min(sequencias_validas, key=lambda s: abs(sum(s) - soma_ultima_sequencia))

  return sequencia_escolhida

# Exemplo de uso
sequencia_gerada = gerar_proxima_sequencia("results.txt")
print(sequencia_gerada)

