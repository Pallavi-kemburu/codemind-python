n=int(input())
p=[]
h=[]
for i in range(n):
    p.append(int(input()))
for i in range(n):
    h.append(int(input()))
c=0
for i in p:
    for j in h:
        if j>=i:
            h.remove(j)
            break
    else:
        c+=1
print(c)