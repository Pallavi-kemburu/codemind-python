for z in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    j=n-1
    res=[]
    while(i<=j):
        if(i==j):
            res.append(l[i])
            break
        res.append(l[j])
        res.append(l[i])
        i+=1
        j-=1
    print(*res)