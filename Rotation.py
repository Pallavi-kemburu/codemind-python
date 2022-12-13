for _ in range(int(input())):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    if p>n:
        p=p%n
    k=[]
    for i in a:
        k.append(i)
    for i in a:
        k.append(i)
    #print(k)
    print(*k[n-p:2*n-p])
        