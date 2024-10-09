#!/usr/bin/python3

l1=[-1,23,-12,0,98,45,12,334,1]
l2=[]

print("list before sorting",l1)
while l1:
    min=l1[0]
    for e in l1:
        if min>e:
            min=e
    l2.append(min)
    l1.remove(min)
print("sorted list:",l2)

