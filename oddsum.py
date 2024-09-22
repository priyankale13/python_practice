#!/usr/bin/python3

n=int(input("Enter a number:"))

sum=0
for i in range(n):
    if i%2!=0:
        sum=sum+i
print("sum of all odd numbers till ",n,":",sum-1)
