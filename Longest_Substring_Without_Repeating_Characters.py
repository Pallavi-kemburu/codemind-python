a=input()
res=[]
r=""
z=[]
for i in range(len(a)):
    r=""
    for j in range(i,len(a)):
        if a[j].lower() not in r.lower():
            r=r+a[j]
        else:
            res.append(r)
            z.append(len(r))
            r=""
if max(z)<3:
    print(-1)
else:
    ind=z.index(max(z))
    print(res[ind])           