from itertools import permutations
n,p=map(int,input().split())
k=[]
for i in range(1,n+1):
    k.append(i)
z=permutations(k)
l=0
for i in z:
    l=l+1
    if l==p:
        s=i
        #g="".join(str(i))
        #print(g)
for i in s:
    print(i,end='')