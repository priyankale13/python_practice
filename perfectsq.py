#!/usr/bin/python3

n=int(input("Enter numberto check for perfect square:"))
odd=1
if n==0:
    print("perfect square")
while n>0:
    n=n-odd
    odd=odd+2
if(n!=0):
    print("not a perfect square")
        
else: 
    print("perfect square")
    
