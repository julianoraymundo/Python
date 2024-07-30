# este é um jogo de adivinhar o numero
import random
secretNumber = random.randint(1,20)
print('estou pensando em um numero de 1 a 20')

# pedindo ao jogador para inserir um numero
for guessesTaken in range(1,7):
    print('Tente adivinhar o numero')
    guess = int(input())

    if guess < secretNumber:
        print('seu numero inserido é muito baixo')
    elif guess > secretNumber:
        print('seu numero inserido é muito alto')
    else:
        break

if guess == secretNumber:
    print('Bom trabalho! voce adivinhou o numero secreto em ' + str(guessesTaken) + ' tentativas')
else:
    print('que pena o numero secreto era ' + str(secretNumber))