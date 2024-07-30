def rounds_validator(k):
    if k != int(4):
        global r_level
        r_level = level - 4
    return r_level

turns = int(input())
for t in range(turns):
    global level, state
    level, state = list(map(int, (input().split())))
    if state == int(1) and level > int(0):
        print('ambiguous')
    else:
        print(level)
        r_validator = rounds_validator(level)
        while r_validator > 4:
            r_validator = rounds_validator(r_validator)
            print(r_validator)

        if r_validator == int(0) and int(state) != int(1):
            print('off')
        else:
            print('on')

