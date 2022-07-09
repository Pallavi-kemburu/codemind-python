def happy(n):
    x=n
    z=0
    while x:
        c=x%10
        z=(z+(c*c))
        x=x//10
    return z
s=int(input())
while s>9:
    s=happy(s)
if  s==1 or s==7:
    print(True)
else:
    print(False)