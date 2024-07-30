cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# exmeplo abaixo de uma atribuiçao expandida
spam = 42
spam += 1 # utilizando essa forma é a mesma coisa que fazer spam = spam + 1
# essa atribuição expandida funciona para todos os operadores, ex: +, -, *, /, %
print(spam)

# os mesmos operadores também podem fazer a concatenaçao de strings ou a repeticao como nos exemplos abaixo
spam = 'hello'
spam += ' world'
print(spam)

bacon = ['sofia']
bacon *= 3
print(bacon)