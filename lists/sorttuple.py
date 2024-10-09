#!/usr/bin/python3

l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
l1=[]
while l1:
    min=l[0]
    for i in l:
        if min>i:
            min=i   
    l1.append(i)
    l.remove(i)

print(l1)
