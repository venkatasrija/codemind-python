num=int(input())
while True:
    d=num%10
    n=num//10
    num=n+d
    if num<10:
        print(num)
        break