#!/usr/bin/python3

price=int(input("Enter price of bike :RS."))

if price>100_000:
    tax=0.15*price
    insurance=0.2*price
    print("Road Tax(15%)= Rs.",tax,"Insurance(20%)= Rs.",insurance)

elif 50_000<price<=100_000:
    tax=0.1*price
    insurance=0.08*price
    print("Road Tax(10%)= Rs. ",tax,"Insurance(8%)=Rs. ",insurance)

elif price<=50_000:
    tax=0.05*price
    insurance=0.05*price
    print("Road tax(5%)=Rs. ",tax,"Insurrance(5%)=Rs. ",insurance)
