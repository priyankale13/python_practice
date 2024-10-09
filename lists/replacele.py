#!/usr/bin/python3

l1=[5,20,15,20,25,50,20]

print("original list:",l1)
for idx in range(len(l1)):
    if l1[idx]==20:
        l1[idx]=200
        print("list after replacement:",l1)
        break

else:
    print("20 not found")
