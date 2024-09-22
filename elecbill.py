#!/usr/bin/python3

units = int(input("Enter no. of units"))
bil=0

if units<=100:
    bill=0

elif 100<units<=200:
    remunits=units-100
    bill=remunits*5
    print("Bill = Rs. ",bill)

elif units>200:
    remunits=units-200
    bill=remunits*10+500
    print("Bill = Rs. ",bill)
else:
    print("Invalid input")

