#!/usr/bin/python3

l1=[1,3,2,6,3,1]
l2=[9,0,'ji']
l3=[]
count=0
for e1 in l1:
    for e2 in l2:
        if e1==e2:
            count+=1
            l3.append(e1)
print(l1,l2)
print(l3)
if count>=1:
    print(True)
else:
    print(False)
print(count)

#compare using any()

for e1,e2 in zip(l1,l2):
    if any(e1==e2):
        print("matching value")
