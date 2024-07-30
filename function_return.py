import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'o numero informado é 1'
    elif answerNumber == 2:
        return 'o numero informado é 2'
    elif answerNumber == 3:
        return 'o numero informado é 3'
    elif answerNumber == 4:
        return 'o numero informado é 4'
    elif answerNumber == 5:
        return 'o numero informado é 5'
    elif answerNumber == 6:
        return 'o numero informado é 6'
    elif answerNumber == 7:
        return 'o numero informado é 7'
    elif answerNumber == 8:
        return 'o numero informado é 8'
    elif answerNumber == 9:
        return 'o numero informado é 9'

print(getAnswer(random.randint(1,9)))


