n=int(input())
d=0
for i in range(1,n//2+1):
    if n%i==0:
        d=d+i
if n==d:
    print("True")
else:
    print("False")
        
        