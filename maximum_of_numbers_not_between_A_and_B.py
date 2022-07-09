n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
f=0
z=[]
for i in a:
    if i<b or i>c:
        f=1
        z.append(i)
if f==0:
    print(-1)
print(max(z))