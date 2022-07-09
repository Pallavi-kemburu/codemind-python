n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i==0 or i==1:
        f=1
    else:
        f=0
        print(False)
        break
if f==1:
    print(True)