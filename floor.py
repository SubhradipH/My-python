import math
def d(n):
    while n>10:
        if n%2==0:
            n = math.floor((n - 2) / 2)
        else:
            n = math.floor(n / 2)
    return n
n=int(input())
print(d(n))