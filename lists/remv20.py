#!/usr/bin/python3

l1=[5,10,20,15,20,25,50,20]
print(l1)
for e in l1:
    if e==20:
        l1.remove(e)

print("after removal of 20, list:",l1)
