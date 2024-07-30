# como exibir os valores de uma lista
# modo feito por mim utilizando um for básico 
a = [1,2,3,4]
for i in a:
  print(i)

# passando um range e lendo o tamanho da lista
a = [1,2,3,4]
for i in range(len(a)):
  print(a[i])

# passando o valor a e posição do valor na lista
a = [1,2,3,4]
for index, value in enumerate(a):
  print(value)
  print(index)


