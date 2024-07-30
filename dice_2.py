import random

turns = int(input())

for i in range(turns):
    dice1, dice2 = list(map(int,input().split()))
    dice_result = dice1 + dice2
    if dice_result > 6:
        print('YES')
    else:
        print('NO')

