#!/usr/bin/python3

n=input("enter a floating point number")

l1=[int(e) for e in n if  e.isdigit()]
#print(str(l1))
if l1[-1]%2==0:
    print(1)
else:
    print(0)
