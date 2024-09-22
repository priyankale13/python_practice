#!/usr/bin/python3

import math

n=int(input("Enter a number:"))
terms=int(input("Enter number of terms :"))
sum=0

for i in range(1,terms):
    fact=math.factorial(i)
    sum=sum+((n**i)/fact)
print("sum of ",terms,":",sum+1)
