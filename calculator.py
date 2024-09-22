#!/usr/bin/python3

import math

print("Calulator Menu")
print("type 1 for add")
print("type 2 for subtract ")
print("type 3 for divide ")
print("type 4 for multiply ")
print("type 5 for integer divion")
print("type 6 for mod operation ")
print("type 7 for check if both numbers are same ")
print("type 8 for squareroot of both numbers ")
print("type 9 for log of both numbers ")
print("type 10 for GCD ")
print("type 11 for LCM ")
ch=int(input("Enter your choice:"))

num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))

match ch:
    case 1:
        print("sum = ",num1+num2)
    case 2:
        print("sub = ",num1-num2)
    case 3:
        print("divide, quotient =",num1/num2)
    case 4:
        print("multiply, product=",num1*num2)
    case 5:
        print("Integer division=",num1//num2)
    case 6:
        print("modulo operation,remainder= ",num1%num2)
    case 7:
        print("are both numbers equal= ",(num1==num2))
    case 8:
        print("square root of:",num1,":",math.sqrt(num1))
        print("square root of:",num2,":",math.sqrt(num2))
    case 9:
        print("log of ",num1,":",math.log10(num1))
        print("log of ",num2,":",math.log10(num2))
    case 10:
        print("GCD = ",math.gcd(num1,num2))
    case 11:
        print("LCM = ",math.lcm(num1,num2))
    case _:
        print("Invalid input")

