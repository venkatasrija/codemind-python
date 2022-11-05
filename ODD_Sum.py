n=int(input())
d=list(map(int,input().split()))
sum=0
for i in d:
    if i%2:
        sum=sum+i
print(sum)    