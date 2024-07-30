spam = ['mouse', 'cat', 'bola', 1, 2, 3, 4] # cria a lista
lista = ['rato', 'gato', 'ball', 5, 6, 7, 8] # cria a lista
print(spam) # chama a lista
print(spam[0]) # chama o indice 0 da lista
print(spam[1]) # chama o indice 1 da lista
print(spam[:5]) # chama o indice 0, 1 2, 3, e 4 sem contar o indice 5
print(spam[3:5]) # chama o indice 3 e 4, sem contar o indice 5
print(spam[4:]) # chama o indice 4 até o ultimo indice
print(spam[-3]) # chama o indice 3 contando de tras para frente (reverso)
print(spam[:-2]) # chama o indice 2 contando de tras para frente (reverso) até o indice 0
print()
print(len(spam)) # chama a lista e informa o seu tamanho (len)
spam[0] = 'bola' # atibui ao indice 0 da lista o valor contido na string
print(spam[0]) # chama o indice 0 da lista
spam[3] = spam[5] # atribui ao indice 3 o valor contido no indice 5
print(spam[3]) # chama o indice 3 da lista
print(spam[5]) # chama o indice 5 da lista
print(spam + lista) # concatena duas listas na tela
print(spam * 2) # exibe 2 vezes a mesma lista na tela
print(spam[2])
del spam[2] # remove o indice 2 da lista
print(spam[2])
