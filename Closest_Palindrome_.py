def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def is_palin(n):
    if n==reverse(n):
        return True
    else:
        return False
def pre_palin(n):
    n=n-1
    while is_palin(n)==False:
        n=n-1
    return n
def next_palin(n):
    n=n+1
    while is_palin(n)==False:
        n=n+1
    return n
x=int(input())
p=pre_palin(x)
n=next_palin(x)
if x-p<n-x:
    print(p)
elif n-x<x-p:
    print(n)
else:
    print(p,n)
    
    
    