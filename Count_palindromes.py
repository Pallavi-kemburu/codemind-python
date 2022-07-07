def palindrome(n):
    a=n
    p=0
    while n:
        r=n%10
        n=n//10
        p=p*10+r
    if a==p:
        return 1
    return 0

n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(palindrome(i)):
        c=c+1
print(c)