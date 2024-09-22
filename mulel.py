#!/usr/bin/python3

l1=[]
mul=1

n=int(input("input no of elemts in list:"))

for e in range(n):
    el=int(input())
    l1.append(el)
    mul=mul*el
print("l1=",l1)
print("product of list elements:",mul)
    
