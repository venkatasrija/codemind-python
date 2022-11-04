n=int(input())
d=list(map(int,input().split()))
ei=0
for i in range(len(d)):
    if i%2==0:
        ei=ei+d[i]
print(ei)        