n=int(input())
a=list(map(int,input().split()))
p=int(input())
if a.count(p)>0:
    print(True)
else:
    print(False)