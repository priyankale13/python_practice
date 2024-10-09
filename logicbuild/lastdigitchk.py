#!/usr/bin/python3
l1=[]

while(len(l1)<4):
    for i in range(3):
        n=int(input("enter a whole number:"))
        if n>0:
            l1.append(n)
        else:
            print("invalid input try again")

print("numbers entered are:",l1)


if l1[0]%10==l1[1]%10 or l1[0]%10==l1[-1]%10 or l1[1]%10==l1[2]%10:
    return 1
else:
    return 0

    
