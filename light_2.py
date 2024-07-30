turns = int(input())
for _ in range(turns):
    mov, state = list(map(int, input().split()))
    if mov != 0 and state == 1:
        print('ambiguous')
    elif mov == 0 and state == 0:
        print('off')
    elif mov % 4 == 0 and state == 0:
        print('off')
    else:
        print('on')



