n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
for i in range(c,b-1,-1):
    if i in a:
        print(i)
        break
else:
    print(-1)