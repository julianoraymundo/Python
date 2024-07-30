tries = int(input())
for i in range(tries):
    seq = list(input())
    pos = 0
    total = 0
    for pos in range(int(len(seq))):
        if int(seq[pos]) == 4:
            total = total + 1
            pos = pos + 1
        else:
            pos = pos + 1
    print(total)