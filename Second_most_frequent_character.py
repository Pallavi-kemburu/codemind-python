a=input()
z=[]
x=[]
for i in a:
    c=a.count(i)
    if c>1 and i not in z:
        z.append(i)
        x.append(c)
x=sorted(set(x))
#print(z,x)
if(len(z)>=1):
    for i in a:
        if a.count(i)==x[-2]:
            print(i)
            break
        
else:
    print(-1)