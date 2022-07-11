s=input()
p=input()
c=0
for i in s:
    if i is p:
        print(True)
        print(s.index(i))
        break
else:
    print(False)