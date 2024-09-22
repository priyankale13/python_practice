#!/usr/bin/python3

n=int(input("input value of x:"))
terms=int(input("input number of terms:"))
sum=0
power=1
for i in range(terms):    
    
    num=n**power
    if i%2==0:
        print(num)
        sum=sum+num
    else:
        print(-num)
        sum=sum-num
    power=power+2
    
print("sum is :",sum)
