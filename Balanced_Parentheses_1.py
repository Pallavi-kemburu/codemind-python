a=input()
k=[]
for i in range(len(a)):
    if a[i]=="(" or a[i]=="[" or a[i]=="{":
        k.append(a[i])
    elif a[i]==")" and k[len(k)-1]=="(" and len(k)!=0:
        k.pop()
    elif a[i]=="]" and k[len(k)-1]=="[" and len(k)!=0:
        k.pop()
    elif a[i]=="}" and k[len(k)-1]=="{" and len(k)!=0:
        k.pop()
    else:
        break
if len(k)==0:
    print("True")
else:
    print("False")