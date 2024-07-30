def divide_com_erro(n1, n2):
  return n1 / n2

def divide_sem_erro(n1, n2):
  try:
    return n1 / n2
  except:
    print('Falha ao calcular')