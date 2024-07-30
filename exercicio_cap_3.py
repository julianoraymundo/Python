# exercicio que ensina a utilizar a sequencia de collatz
def collatz(number):
    if number % 2 == 0:
      answer = int(number) // 2
      print(number)
      return answer
    elif number % 2 == 1:
        answer = 3 * int(number) + 1
        print(number)
        return answer

while True:
    try:
        num = int(input('informe um numero '))
        break
    except:
        print('numero informado não é um inteiro')

while num != 1:
    num = collatz(num)

