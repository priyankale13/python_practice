#!/usr/bin/python3
import string
def countcase(str1):
    countl=0
    countu=0
    for e in str1:
        if e.islower():
            countl+=1
        if e.isupper():
            countu+=1
    return countl, countu        

st=input("enter a string in mixed cases")
print("no of upper and lower case character :(lowercase,uppercase):")
print(countcase(st))
