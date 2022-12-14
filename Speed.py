for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    for i in range(n-1):
        if a[i]>=a[i+1]:
            c=c+1
    print(c)