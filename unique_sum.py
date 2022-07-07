n=int(input())
a=list(map(int,input().split()))
c=[]
s=0
for i in a:
    if i not in c:
        c.append(i)
        s=s+i
print(s)