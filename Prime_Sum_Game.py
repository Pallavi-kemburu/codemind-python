def prime(n):
    if n==1:
        return 1
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return 0
        return 1
k=[]
a,b,c,d=map(int,input().split())
for i in range(a,b+1):
    f=0
    for j in range(c,d+1):
        if prime(i+j):
            f=1
    k.append(f)
#print(k)
#print(k.count(0))
if all(k):
    print("Aoki")
else:
    print("Takahashi")