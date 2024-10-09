#!/usr/bin/python3
l1=[10,20,30,40,50]
l2=[100,200,300,400,500]

for i,j in zip(l1,l2[::-1]):
    print(i,end=' ')
    print(j)
    print(sep='')
    
