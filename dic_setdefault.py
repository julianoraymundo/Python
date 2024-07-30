import pprint
spam = {'nome': 'juliano', 'idade': 30}
spam.setdefault('genero', 'homem')
print(spam)

mensagem = 'É muito interessante como os cachorros tem suas personalidades e se acosumam com a personalidade de seu dono'
count = {}

for caracter in mensagem:
    count.setdefault(caracter, 0)
    count[caracter] = count[caracter] + 1
pprint.pprint(count)
print(pprint.pformat(count))