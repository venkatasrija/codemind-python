n=int(input())
d=list(map(int,input().split()))
s=0
for ele in d:
    s=s+ele
    t=s//len(d)
if t in d:
    print("True")
else:
    print("False")
    