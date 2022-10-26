n=int(input())
a=[]
s1=0
s2=0
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(n):
    for j in range(n):
        if i==j:
            s1=s1+a[i][j]
            #print(a[i][j])
        if (i+j)==n-1:
            s2=s2+a[i][j]
#print(a)
print("Principal Diagonal:"+str(s1))
print("Secondary Diagonal:"+str(s2))