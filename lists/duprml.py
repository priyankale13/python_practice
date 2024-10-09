#!/usr/bin/python3

l1=[2,3,1,1,3,5,6,7,7,5,4,9,0,2,3,5]
l2=[]
l2.append(l1[0])
print(l1)
for e in range(1,len(l1)):
    for i in range(len(l2)):    
        if  l1[e]==l2[i]:
            break
    else:        
        l2.append(l1[e])
print(l2)
