def fact(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+i
    return s
a=list(map(int,input().split(",")))
k=[]
for i in a:
    s=fact(i)
    if s in a:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    k.sort()
    print(*k)