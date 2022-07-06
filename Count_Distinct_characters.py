s=input()
s=s.lower()
k=""
for i in s:
    if i not in k and i!=' ':
        k+=i
print(len(k))