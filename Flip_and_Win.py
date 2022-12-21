n=int(input())
s=input()
c=0
for i in range(0,n-1):
    c+=(abs(int(s[i+1])-int(s[i])))
c=n-c-1
if c%3==0:
    print('Sudhir')
else:
    print("Ashok")