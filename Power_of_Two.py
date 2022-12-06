import math as m
n=int(input())
for i in range(-31,31):
    if (2**i)==n:
        print("True")
        break
else:
    print("False")