spam = 1
while spam < 10:
	print('teste com while ' + str(spam))
	spam = spam + 1

name = ''
while name != 'seu nome':
	print('informe seu nome')
	name = input()
	if name == 'seu nome':
		break
print('obrigado')

while True:
	print('quem é voce?')
	name = input()
	if name != 'Joe':
		continue
	print('ola Joe, qual é a senha? (é um peixe)')
	password = input()
	if password == 'swordfish':
		break
print('acesso garantido')


