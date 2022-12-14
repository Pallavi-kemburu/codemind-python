a=input().lower()
k=[]
s="aeiou"
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[j] in s:
            c=c+1
        else:
            k.append(c)
            c=0
k.append(c)
print(max(k))