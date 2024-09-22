#!/usr/bin/python3
import string

total_classes = int(input("Enter total number of classes: "))
total_attend  = int(input("Enter total no. of classes attended: "))

per_attend = total_attend/total_classes *100

print("Your attendance is :",per_attend)
if (per_attend>= 75):
   print("You can take exam")
else:
    ans=input("Does student have medical cause:").lower()
    if (ans=='y'):
        print("You  are allowed to take exam")
    else:
       print("You are not allowed to take exam")


