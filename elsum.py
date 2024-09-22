#!/usr/bin/python3

l1=[]
sum=0
n=int(input("enter no of elemets in list:"))
for e  in range(n):
    el = int(input())
    l1.append(el)
    sum=sum+el

print("l1=",l1)
print("sum of elemets:",sum)
