# swapping two numbers 
'''a=1
b=2
a,b=b,a
print(a,b)  
'''
# swapping two numbers using 3rd variable
'''a=1
b=2
c=a
a=b
b=c
print(a,b)   # output: 2 1
'''
# swapping two numbers using XOR operator
'''a=1
b=2
a=a^b
b=a^b
a=a^b
print(a,b)   # output: 2 1
'''

# factorial
'''
n=int(input("enter the number : "))

fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
'''
# fibonacci series
'''n=int(input("enter the number : "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
'''

#prime number
'''n=int(input("enter the number : "))
for i in range(2,n):
    if n%i==0:
        print(n,"is not a prime number")
        break
    else:
        print(n,"is a prime number")
        break
'''

# max
'''a=1
b=1000
c=100
print(max(a,b,c))
'''
# second largest 
num=[int(input("enter the numbers: ")) for _ in range(10)]
num.sort(reverse=True)
print(num[1])