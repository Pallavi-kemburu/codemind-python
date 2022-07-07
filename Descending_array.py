n=int(input())
a=list(map(int,input().split()))
c=0
m=10000
for i in a:
    if i<m:
        m=i
        c=c+1
if c==n:
    print('yes')
else:
    print('no')