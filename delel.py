#!/usr/bin/python3

l1=["Ashish", "", "Atharva", "", "Amit", "Revati"]

print("l1:",l1)

l1[:]=[e for e in l1 if e]

print("list after deleting empty strings:",l1)
