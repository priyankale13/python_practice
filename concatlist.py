#!/usr/bin/python3

l1=[5, 6, 7]
l2=[0, 1]

print("l1=",l1)
print("l2=",l2)
l3=[(e1*10+e2) for e1 in l1 for e2 in l2]
print("res=",l3)
