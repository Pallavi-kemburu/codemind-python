n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if i not in c and i%2!=0:
        c.append(i)
print(len(c))