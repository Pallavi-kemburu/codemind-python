s=input()
b=s.count('b')
a=s.count('a')
l=s.count('l')
o=s.count('o')
n=s.count('n')
#print(b,a,l,o,n)
z=[]
z.append(b)
z.append(a)
z.append(l//2)
z.append(o//2)
z.append(n)
if len(z)==5:
    print(min(z))
else:
    print(0)