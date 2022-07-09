n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
z=[]
for i in l:
    if i>=a and i<=b:
        z.append(i)
if len(z)==0:
    print(-1)
else:
    print(*z)