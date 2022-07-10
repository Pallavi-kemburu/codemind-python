n=int(input())
a=list(map(int,input().split()))
f=0
for i in range(2,n):
    if a[i]==a[i-1]+a[i-2]:
        f=1
    else:
        f=0
        break
if f==0:
    print('no')
else:
    print('yes')