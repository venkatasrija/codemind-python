n=int(input())
es=0
os=0
data=list(map(int,input().split()))
for i in data:
    if i%2==0:
        es=es+i
    else:
        os=os+i
dif=abs(os-es)
print(dif)