def digit(n):
    s=0
    while n:
        q=n%10
        n=n//10
        s=s+q
    return s
n=int(input())
a=list(map(int,input().split()))
p=0
for i in a:
    s=digit(i)
    p=p+s
print(p)