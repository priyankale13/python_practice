#!/usr/bin/python3
l2=[]
l1=[12,90,-7,-56,99]
print(l1)
min=l1[0]
for i in range(len(l1)):
    for e in l1:
        if min>e:
            min=e
        l2.append(e)
        l1.remove(e)

print("second lowest:",l2[1])
    
    
