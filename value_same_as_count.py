n=int(input())
a=list(map(int,input().split()))
c=0
z=[]
for i in a:
    if a.count(i)==i and i not in z:
        z.append(i)
        c=c+1
print(c)