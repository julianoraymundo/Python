spam = []
while True:
    print('Informe um valor para a lista '  + str(len(spam) + 1) + ' (Ou nada para parar):')
    name = input()
    if name == '':
        break
    spam = spam + [name]

for i in range(len(spam[:-1])):
   print(str(spam[i]) + str(','))

print(str(' and ') + str(spam[-1]))