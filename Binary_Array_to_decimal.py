n=int(input())
a=list(map(int,input().split()))
d=0
p=0
for i in range(n-1,-1,-1):
    d=d+(2**p)*a[i]
    p=p+1
print(d)