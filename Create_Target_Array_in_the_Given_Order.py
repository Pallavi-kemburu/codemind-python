m=int(input())
a=list(map(int,input().split()))
n=input()
k=list(map(int,input().split()))
z=[]
for i in range(m):
    z.insert(k[i],a[i])
print(*z)