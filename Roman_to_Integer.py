z={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input()
s=s[::-1]
r=0
x=0
for i in s:
    if z[i]<x:
        r-=z[i]
    else:
        r+=z[i]
    x=z[i]
print(r)