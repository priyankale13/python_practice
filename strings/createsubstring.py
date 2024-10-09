#!/usr/bin/python3

s=input("enter a string of odd length and > 7:")
if len(s)<7 or len(s)%2==0:
    st=input("string is either less than 7 or even, try again!")
l=len(s)
st=int((l-3)/2)
newst=s[st:(st+3)]
print(newst)
