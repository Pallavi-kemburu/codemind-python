m=int(input())
n=int(input())
s=0
l=[list(map(int,input().split()))for i in range(0,m)]
for i in l:
    for j in i:
        s=s+j
print(s)