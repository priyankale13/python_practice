#!/usr/bin/python3

n=int(input("Enter a number of terms to generate in series:"))

total=0
for i in range(n):
    term='9'*(i+1)
    total=int(term)+total
    print(term)
print("total addition of terms :",total)
