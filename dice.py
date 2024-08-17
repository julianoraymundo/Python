import random

turns = int(input('Informe quantas vezes os dados irão rolar: '))

for i in range(turns):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result = dice1 + dice2
    if dice_result > 6:
        print('Resultado = ' + str(dice_result) + ' Boa jogada')
    else:
        print('Resultado = ' + str(dice_result) + ' Jogada ruim')

