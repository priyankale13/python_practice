#!/usr/bin/python3

def displayaltchar(str1):
    for idx in range(1,len(str1),2):
        print(str1[idx],end='')
    print(sep='')   
    
st=input("enter a string:")
displayaltchar(st)        
