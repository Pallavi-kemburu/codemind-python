n,p=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    l=len(str(abs(i)))
    if p==l:
        c=c+1
print(c)