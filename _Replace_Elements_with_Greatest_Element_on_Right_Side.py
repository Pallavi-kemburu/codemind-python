n=int(input())
a=list(map(int,input().split()))
p=[]
for i in range(0,n-1):
    k=[]
    for j in range(i+1,n):
        k.append(a[j])
    p.append(max(k))
p.append(-1)
print(*p)