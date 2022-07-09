z=int(input())
a=list(map(int,input().split()))
n=[]
for i in range(0,z,2):
    for j in range(0,a[i+1]):
        n.append(a[i])
print(*n)