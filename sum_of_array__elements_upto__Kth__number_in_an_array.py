n=int(input())
a=list(map(int,input().split()))
p=int(input())
s=0
for i in a:
    s=s+i
    if i==p:
        break
print(s)