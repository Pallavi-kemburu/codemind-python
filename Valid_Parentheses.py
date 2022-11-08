for z in range(int(input())):
    s=input()
    l=[]
    f=0
    for i in s:
        if i=='(' or i=='[' or i=='{':
            l.append(i)
        elif i==')' and len(l)!=0 and l[len(l)-1]=='(':
            l.pop()
        elif i==']' and len(l)!=0 and l[len(l)-1]=='[':
            l.pop()
        elif i=='}' and len(l)!=0 and l[len(l)-1]=='{':
            l.pop()
        else:
            print('False')
            f=1
    if f==0:
        if len(l)==0 :
            print('True')
        else:
            print('False')

