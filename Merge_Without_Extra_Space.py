t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in b:
        a.append(i)
    print(*sorted(a))