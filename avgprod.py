#!/usr/bin/python3

prod=1
total=0
count=0
num=0

while num!='q':
    num=input("Enter an integer, else enter 'q' to quit")
    if num=='q':
        break
    num=int(num)
    total=total+num
    count +=1
    prod=prod*num

print("Product of all no's is ", prod)
print("average of a;; no's is",total/count)
