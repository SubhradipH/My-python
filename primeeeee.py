'''from sympy import *

g1 = isprime(30)
g2 = isprime(13)
g3 = isprime(2)

print(g1) 
print(g2) 
print(g3)
'''

def is_prime(n):
    if n<=0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
