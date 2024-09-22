#!/usr/bin/python3

num=input("Enter a number")
digits=list(num)
last_digit=int(digits[-1])
if last_digit%3==0 :
    print("last digit is divisible by 3")
else:
    print("last digit is not divisible by 3")
