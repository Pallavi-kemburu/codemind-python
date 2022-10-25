a=input()
s=""
for i in a:
    if int(i)%2!=0:
        s=s+str(int(i)*int(i))
print(s)