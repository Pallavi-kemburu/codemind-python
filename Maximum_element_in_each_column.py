m,n=map(int,input().split())
a=[]
k=[]
for i in range(m):
    l=list(map(int,input().split()))
    a.append(l)
for j in range(n):
    s=[]
    for i in range(m):
        s.append(a[i][j])
    k.append(s)
for i in k:
    print(max(i))