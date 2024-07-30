# cook your dish here
tries = int(input())

for i in range(tries):
    cost, mana = list(map(int, input().split()))
    if cost > mana:
        print(0)
    else:
        atacks = mana // cost
        print(atacks)
