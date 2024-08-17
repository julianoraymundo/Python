# cook your dish here
tries = int(input())

for i in range(tries):
    dividendo = int(input())
    j = 0
    for j in range(10):
        j = j + 1
        result = dividendo % j
        print(str(dividendo) + ' / ' + str(j) + ' = ' + str(result))

