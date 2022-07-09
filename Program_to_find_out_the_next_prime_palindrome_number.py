def prime(n):
    if n==1:
        return 0
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
def pali(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==n:
        return 1
    return False
            
n=int(input())
i=n+1
while prime(i)==False or pali(i)==False:
    i=i+1
print(i)