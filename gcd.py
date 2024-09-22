#!/usr/bin/python3

n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))

gcd=1
for i in range(2,n2):
    if(n1%i==0 and n2%i==0):
        gcd=gcd*i
        n1=n1//i
        n2=n2//i
print("GCD =",gcd)

