#!/usr/bin/python3

l1=[]
for num in range(150,250,2):
    l1.append(num)
print("l1=",l1)
print("length of list=:",len(l1))
l2=[e for e in l1 if (e%4==0)]
print("l2=",l2)
