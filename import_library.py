import random, sys

for i in range(5):
    print(random.randint(1, 10))
print()

while True:
    print('escreva sair para sair')
    response = input()
    if response == 'sair':
        sys.exit()
    print('voce digitou ' + response + ' .')

