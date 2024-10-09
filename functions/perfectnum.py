#!/usr/bin/python3

def isperfectnum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if (sum-num)==0:
        print("number is perfect")
    else:
        print("not a perfect number")

n=int(input("enter a positive interger:"))
if n>0 and type(n) is int:
    isperfectnum(n)
else:
    print("enter number is not positive integer")
