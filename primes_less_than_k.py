def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if prime(int(i)):
        if i<=k:
            c=c+1
print(c)