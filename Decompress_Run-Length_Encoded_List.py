n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(1,n,2):
    for j in range(a[i-1]):
        k.append(a[i])
print(*k)