# execício
# como calcular a media de uma lista de valores inteiros

# utilizando interações individuais no array
a = [1,2,3,4]
x = a[0] + a[1] + a[2] + a[3]
y = x / 4
print(y)    

# utilizando as funções do python
def calcular_media(lista_valores):
  return sum(lista_valores) / len(lista_valores)

b = [1, 2, 3, 4]
print(calcular_media(b))

# utilizando o for
a = [1, 2, 3, 4]
def calcular_media(lista):
  total = 0
  for item in lista:
    total += item
  return total / len(lista)
print(calcular_media(a))