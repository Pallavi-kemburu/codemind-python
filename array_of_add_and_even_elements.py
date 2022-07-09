n=int(input())
a=list(map(int,input().split()))
o=[]
e=[]
for i in range(n):
    if a[i]%2!=0:
        o.append(a[i])
    else:
        e.append(a[i])
print(*o,end=' ')
print(*e,end=' ')