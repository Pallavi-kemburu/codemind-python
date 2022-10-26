n=int(input())
a=list(map(int,input().split()))
p=[]
for i in range(0,n-1):
    k=[]
    for j in range(i+1,n):
        k.append(a[j])
    if(a[i]<max(k)):
        p.append(max(k)-a[i])
if(len(p)==0):
    print(0)
else:
    print(max(p))