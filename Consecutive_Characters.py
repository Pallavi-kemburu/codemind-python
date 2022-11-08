a=input()
z=[]
c=1
for i in range(len(a)-1):
        if a[i]==a[i+1]:
            c=c+1
        else:
            z.append(c)
            c=1
z.append(c)
print(max(z))