#!/usr/bin/python3

l1=[11,23,22,34,67,89,90,55,33]

def divisible11(l):
    for e in l:
        if e%11==0:
            print(e)

divisible11(l1)
