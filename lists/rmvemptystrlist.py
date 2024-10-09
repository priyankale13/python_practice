#!/usr/bin/python3

l1=['atharva','ashish','','revati','','amitabh','','jenny','ritesh',]
print("original list:",l1)
for st in l1:
    if st=='':
        l1.remove(st)


print("after removing empty strings, list:",l1)

