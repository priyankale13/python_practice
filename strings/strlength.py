#!/usr/bin/python3

str1='hello world!, welcome to iacsd'

#without using built-in function
count=0
for e in str1:
    count+=1

print(f"length of string is:{count}")

#using builtin function

print(f"length of string is (using builtin function):{len(str1)}")
