n=int(input())
d=list(map(int,input().split()))
oi=0
for i in range(len(d)):
    if i%2:
        oi=oi+d[i]
print(oi)        