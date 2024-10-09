#!/usr/bin/python3


n=int(input("enter an positive integer:"))

while int(n)<0 :
    n=input("not a positive integer, enter again:")

numlist=list(str(n))
numlist.sort()
minnum=''.join(numlist)
print("minimum number:",minnum)

maxnum=minnum[::-1]
print("maximum number:",maxnum)
