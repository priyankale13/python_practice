#!/usr/bin/python3

str1=input("Enter a string:")

def ispalindrome(st):
    if st[::-1]==st:
        return 1
    else:
        return 0

if (ispalindrome(str1)):
    print("palindrome")
else:
    print("not a palindrome")
