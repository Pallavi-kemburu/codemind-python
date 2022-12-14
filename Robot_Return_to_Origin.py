a=input().lower()
l=a.count('l')
u=a.count('u')
r=a.count('r')
d=a.count('d')
if (l==r) and (u==d):
    print("True")
else:
    print("False")