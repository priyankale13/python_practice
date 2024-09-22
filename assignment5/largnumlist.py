#!/usr/bin/python3

l1=[]
n=int(input("Enter size of list:"))
print("Enter elemts of list:")
max=0
for e in  range(n):
    num=int(input())
    l1.append(num)
    if max<num:
        max=num

print("largest  element in list:",max)
print("l1=",l1)
