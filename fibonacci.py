def fib_gen():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = c + a
        yield c # yield is a function that runs only once on the fly not on memory

f = fib_gen()
for i in range(20):
    print(next(f), end=' ') # the next function is needed to print the next value of the yield iterator
