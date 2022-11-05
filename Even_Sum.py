n=int(input())
d=list(map(int,input().split()))
es=0
for i in d:
    if i%2==0:
        es=es+i
print(es)        