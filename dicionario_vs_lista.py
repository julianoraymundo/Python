spam = ['cats', 'dogs', 'mouse']
bacon = ['dogs', 'cats', 'mouse']
print(spam == bacon)

eggs = {'nome': 'juliano', 'especie': 'humano', 'idade': '29'}
ham = {'especie': 'humano', 'nome': 'juliano', 'idade': '29'}
print(eggs == ham)

# as listas para serem consideradas True ou iguais, precisam ser identificas em seus indices.
# os dicionarios nao precisam respeitar as mesmas posicoes, somente os atributos de chave-valor
# da mesma forma que as listas os dicionarios podem ser fatiados
print()
for v in eggs.values():
    print(v)
print()
for k in eggs.keys():
    print(k)
print()
for i in eggs.items():
    print(i)