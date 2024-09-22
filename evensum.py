#!/usr/bin/python3

sum=0
for i in range(20):
    num=int(input("Enter a number"))
    if num%2==0:
        sum=sum+num

print("sum of even numbers entered:",sum)
