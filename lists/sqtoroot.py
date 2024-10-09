#!/usr/bin/python3

import math

l1=[1,4,9,16,25,36,49,64,81]
print("list containig squares:",l1)

#using builtin function
l2=[int(math.pow(x,0.5)) for x in l1]
print("squareroot list using built in function :",l2)

#without using built in function

l3=[]
for num in l1:
    for i in range(1,num+1):
        if num/i==i:
            l3.append(i)
print("sqaureroot list without using builtin function: ",l3)
