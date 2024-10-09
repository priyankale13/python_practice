#!/usr/bin/python3
import math
def isprime(num):
    if num==2:
        return 1
    if num!=2 and num%2==0:
        return 0
    for i in range(3,int(math.sqrt(num))):
        if num%i==0:
            break
    else:
        return 1


n=int(input("Enter a number to check if prime:"))
if isprime(n):
    print("Prime number")
else:
    print("Not a prime number")

