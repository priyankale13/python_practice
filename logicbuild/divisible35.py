#!/usr/bin/python3
l1=[]
l2=[]
l3=[]
for i in range(1,101):
    if i%3==0:
        l1.append(i)
    if i%5==0:
        l2.append(i)
    if i%3==0 and i%5==0:
        l3.append(i)
print('numbers divisible by 3',l1)
print('numbers divisible by 5',l2)
print('numbers divisible by 3 and 5',l3)        
