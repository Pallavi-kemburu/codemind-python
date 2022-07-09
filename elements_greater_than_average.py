n=int(input())
a=list(map(int,input().split()))
#print(a)
c=0
s=sum(a)/n
for i in a:
    if i>=int(s):
        #print(i)
        c=c+1
print(c)