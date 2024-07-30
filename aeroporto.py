#
# (1 <= X1 , Y1 , X2 , Y2 <= 8)
# A dama começa na casa de coordenadas (X1 , Y1)
# e a casa de destino é a casa de coordenadas (X2 , Y2).
# O final da entrada é indicado por uma linha contendo quatro zeros.
# Para cada caso de teste da entrada seu programa deve imprimir uma unica linha na saída, contendo um número inteiro,
# indicando o menor número de movimentos necessários para a dama chegar em sua casa de destino.
# Entrada
# 4 4 6 2
# 3 5 3 5
# 5 5 4 3
# 0 0 0 0

# Saída
# 1
# 0
# 2

x1 = input()
y1 = input()
x2 = input()
y2 = input()

while x1 and y2 and x2 and y2 != int(0):
    inicial_x1 =