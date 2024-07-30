meusPets = ['lucy', 'jack', 'gibson', 'amy', 'mel']
print('informe o nome do seu pet')
name = input()
if name not in meusPets:
    print('desculpe mas nao temos nenhum pet chamado de ' + str(name))
else:
    print(str(name) + ' é o meu pet')