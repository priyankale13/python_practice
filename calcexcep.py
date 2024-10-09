#!/usr/bin/python3
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    b=valid_deno_input()
    return a/b, a%b
def valid_int_input():
    while True:
        try:
            num=input("enter a number:")
            num=int(num)
        except ValueError:
            print("enter valid integer")
        else:
            break        
    return num

def valid_choice_input():
    while True:
        try:
            num=input("enter choice:")
            num=int(num)
        except ValueError:
            print("enter a valid integer")
        else:
            break
    return num 

def valid_deno_input():
    while True:
        try:
            num==0
        except ZeroDivisionError:
            print("you are trying to use /0")
        print("completed") 


print("-------------------calculator menu----------------------")
print("type 1 for addition")
print("type 2 for subtraction")
print("type 3 for multiplication")
print("type 4 for division")
print("type 5 to quit")
print("--------------------------------------------------------")
ch=valid_choice_input()
n1=valid_int_input()
n2=valid_int_input()
match ch:
    case 1:
        print("you have selected addition")  
        print(addition(n1,n2))
        
    case 2:
        print("you have selected subtraction")
        subtraction(n1,n2)
        
    case 3:
        print("you have selected multiplication")
        multiplication(n1,n2)
        
    case 4:
        print("you have selected division")
        division(n1,n2)
    case _:
        print("invalid input")
if int(ch)==5:
    print("quiting....")


