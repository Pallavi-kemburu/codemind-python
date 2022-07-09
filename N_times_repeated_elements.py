n=int(input())
a=list(map(int,input().split()))
p=int(input())
c=[]
f=0
for i in a:
    if a.count(i)==p and i not in c:
        f=1
        c.append(i)
        print(i,end=' ')
if f==0:
    print(-1)