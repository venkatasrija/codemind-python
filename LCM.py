def lcm(n,m):
    b=max(n,m)
    p=b
    while True:
        if b%n==0 and b%m==0:
            l=b
            break
        b=b+p
        
    return l
n,m=map(int,input().split())
res=lcm(n,m)
print(res)