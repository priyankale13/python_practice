#!/usr/bin/python3

amount=int(input("Enter the amount:"))

if(amount>=2000):
    note_2k=amount//2000
    amount=amount%2000
    print("note_2k = ",note_2k)
if(amount>=500):
    note500=amount//500
    amount=amount%500
    print("note500 = ",note500)
if(amount>=100):
    note100=amount//100
    amount=amount%100
    print("note100 = ",note100)
if(amount>=50):
    note50=amount//50
    amount=amount%50
    print("note50= ",note50)
if(amount>=10):
    note10=amount//10
    amount=amount%10
    print("note10= ",note10)
if(amount>=5):
    note5=amount//5
    amount=amount%5
    print("note5 = ",note5)
if(amount>=2):
    note2=amount//2
    amount=amount%2
    print("note2= ",note2)
if(amount>=1):
    note1=amount//1
    amount=amount%1
    print("note1 = ",note1)
 
