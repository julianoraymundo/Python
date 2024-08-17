# import de bibliotecas
import os

# Definição de variáveis de ambiente do host
hostname = os.getenv('HOSTNAME')
username = os.getenv('USER')

# Inicio do código
print('Olá ' + username + 'você está logado em ' + hostname)

num1 = float(input('informe um numero > '))
num2 = float(input('informe outro nmero > '))
operacao = input('informe a operação que deseja fazer + - * /  >')

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print ('operacão não permitida')
    resultado = None

if resultado is not None:
    print(f'o resultado de {num1} {operacao} {num2} é igual a {resultado}.')

while
