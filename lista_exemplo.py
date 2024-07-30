catNames = []
while True:
    print('Informe o nome do seu gato ' + str(len(catNames) + 1) + ' (Ou nada para parar.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # concatenaçao de linhas
print('os nomes dos gatos são')
for name in catNames:
    print(' ' + name)