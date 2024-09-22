#!/usr/bin/python3

num=int(input("enter a number:"))
n=2
while(n<num):
    if num%n==0:
        print("not a prime number")
        break
    n=n+1
else:
    print("Prime number")

