m=int(input())
a1=list(map(int,input().split()))
n=int(input())
a2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if a1[i]<=k and a2[i]>=k:
        c=c+1
print(c)