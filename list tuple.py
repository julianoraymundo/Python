list1 = ['apple', 'banana', 'oranges', 'pomegranate']
tuple1 = ('apple', 'banana', 'oranges', 'pomegranate')

# listamos a lista e a tupla
print(list1[3])
print(tuple1[3])

# aqui mudamos o conteudo do segundo index da lista
list1[2]='pen'
print(list1)

# aqui tentamos mudar o segundo item da tupla, porém não é possivel. 
# apresentando o erro abaixo
# TypeError: 'tuple' object does not support item assignment
#tuple1[2]='pencil'
#print(tuple1)

# aqui conseguimos fazer um merge de tuple1 e tuple2 para tuple3, 
#dessa forma provando os dados imutaveis de tupla
tuple2=('pencil', )
tuple3=tuple1 + tuple2
print(tuple3)

#tuplas também podem ser definidas com chaves de dicionarios
t={('this', 'is'):23, ('is', 'a'): 2, ('re', 'sen'):2}
print(t)

# mas listas não podem, ocasionando o erro abaixo descrito
# TypeError: unhashable type: 'list'
#l={['this', 'is']:23, ['is', 'a']:2, ['re', 'sen']:2}
#print(l)

