n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for ele in l:
    if ele<a or ele>b:
        c=c+ele
print(c)    