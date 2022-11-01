n=int(input())
s=0
d=list(map(int,input().split()))
for ele in d:
    s=s+ele
    t=s/len(d)
print("%.2f"%t)    
    