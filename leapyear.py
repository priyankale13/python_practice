#!/usr/bin/python3

year=int(input("Enter year :"))

if year%400==0:
    print("leap year")
elif (year%100!=0)and(year%4==0):
    print("leap year")
else:
    print("not a leap year")
