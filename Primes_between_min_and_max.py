def prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
a=list(map(int,input().split()))
mi=a.index(min(a))
ma=a.index(max(a))
c=0
if mi<ma:
    for i in range(mi,ma+1):
        if prime(int(a[i])):
            c=c+1
else:
    for i in range(ma,mi+1):
        if prime(int(a[i])):
            c=c+1
print(c)