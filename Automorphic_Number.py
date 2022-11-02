n=int(input())
s=str(n)
k=n*n
p=str(k)
if p.endswith(s):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")