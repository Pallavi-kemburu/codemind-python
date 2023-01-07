n=int(input())
a=list(map(int,input().split()))
b=0
p=-1
while True:
    k=0
    pk=0
    for i in a:
        k=k^(i+b)
        pk=pk^(i+p)
    if k==0:
        print(b)
        break
    elif pk==0:
        print(-1)
        break
    else:
        b=b+1
        p=p-1