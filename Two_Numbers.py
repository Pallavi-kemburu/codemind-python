n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if a.count(i)==1:
        k.append(i)
k.sort()
print(*k)