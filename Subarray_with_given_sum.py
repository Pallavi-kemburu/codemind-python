for _ in range(int(input())):
    n,sm=map(int,input().split())
    a=list(map(int,input().split()))
    k=[]
    for i in range(n):
        s=0
        for j in range(i,n):
            if a[j]==sm:
                k.append(j+1)
                break
            s=s+a[j]
            if(s==sm):
                k.append(i+1)
                k.append(j+1)
                break
            elif (s>sm):
                break
        if(len(k)>0):
            break
    if(len(k)!=0):
        print(*k)
    else:
        print(-1)
            
    