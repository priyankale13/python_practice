#!/usr/bin/python3

def iseven(num):
    if num%2==0:
        print(True)
    else:
        print(False)

n=int(input("Enter an integer number:"))
print("is given number even?")
iseven(n)
