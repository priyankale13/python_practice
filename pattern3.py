#!/usr/bin/python3

n=int(input("Enter no of lines:"))

ten=n-1
sp=0
for line_no in range(n):
    print(" "*sp,"10"*ten,'1',sep="")
   
    ten=ten-1
    sp=sp+1

