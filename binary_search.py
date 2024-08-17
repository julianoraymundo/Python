def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) -1
    count = 0

    while baixo <= alto:
        count += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else: 
            baixo = meio + 1
    return None, count

minha_lista = list(range(0,40000000))

#print(minha_lista)
print(pesquisa_binaria(minha_lista, 78))
print(pesquisa_binaria(minha_lista, -1))