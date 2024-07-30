def rec(n ):
    if n==1:
      return 1
    if n==2:
      return 1
    if n>2:
      return rec(n-1)+rec(n-2)
print(rec(6))


