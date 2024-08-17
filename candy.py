# cook your dish here
tries = int(input())

for i in range(tries):
    chocolate, candy = list(map(int, input().split()))
    chocolate = chocolate * 2
    candy = candy * 5
    if chocolate > candy:
        print('Chocolate')
    elif chocolate == candy:
        print('Either')
    else:
        print('Candy')
