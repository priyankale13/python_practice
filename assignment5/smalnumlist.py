#!/usr/bin/python3

l1=[]
n=int(input("Enter no. of elemts in wnat to add in list.:"))

min=0
for e in range(n):
    num=int(input())
    l1.append(num)
    if min>num:
        min=num

print("l1=",l1)
print("smallest element is:",min)
