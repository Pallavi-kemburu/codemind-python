n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
f=0
for i in a:
    if i<b or i>c:
        f=1
        print(i,end=' ')
if f==0:
    print(-1)