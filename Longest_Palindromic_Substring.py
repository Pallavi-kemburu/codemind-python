def pali(a):
    a=str(a)
    if a==a[::-1]:
        return 1
    return 0
a=input()
k=[]
l=[]
for i in range(len(a)):
    for j in range(len(a)):
        if pali(a[i:j+1]):
            k.append(a[i:j+1])
            l.append(len(a[i:j+1]))
z=l.index(max(l))
#print(z)
print(k[z])