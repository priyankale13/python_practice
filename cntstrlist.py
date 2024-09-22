#!/usr/bin/python3

l1=['abc','xyz','aba','12431']

count=0
for e in l1:
    if len(e)>2:
        if e[0]==e[-1]:
            count=count+1
print("no. of string elements  with length >2 and first and last charcter same:")
print(count)

