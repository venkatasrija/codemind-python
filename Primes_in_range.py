import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
count=0
if a==1:
    a=2
for i in range(a,b+1):
    res=isprime(i)
    if res==True:
        count=count+1
print(count)        