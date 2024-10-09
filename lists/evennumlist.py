#!/usr/bin/python3

l1=[]

i=150

while i<=250:
    l1.append(i)
    i+=2

print("length of list:",len(l1))
print("list is :",l1)

l2=[x for x in l1 if x%4==0 ]
print("list elemets divisible by 4:",l2)
