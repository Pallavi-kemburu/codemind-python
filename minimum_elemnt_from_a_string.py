s=input()
s=s.split()
i=s[-1]
if min(i).lower() in i:
    print(min(i).lower())
else:
    print(min(i))
    