from math import*
def isprime(n):
    if n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
p=0
for i in range(m,n+1):
    if isprime(i):
        p+=1
print(p)        