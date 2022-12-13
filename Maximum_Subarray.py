n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+a[j]
        k.append(s)
print(max(k))