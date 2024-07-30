aniversarios = {'alice': '1 - abril', 'bob': '15 - junho', 'carol': '30 - setembro'}

while True:
    print('Informe o nome: (deixe em branco para sair)')
    name = input()
    if name == '':
        break

    if name in aniversarios:
        print(aniversarios[name] + ' é o aniversario de ' + name)
    else:
        print('Nao tenho informacoes para o ' + name)
        print('qual é o aniversario?')
        bday = input()
        aniversarios[name] = bday
        print('Aniversarios atualizados.')