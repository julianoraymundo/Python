# cook your dish here
tries = int(input())

for i in range(tries):
    candy = int(input())
    result = candy % 3
    if result == 0:
        print('yes')
    else:
        print('no')
