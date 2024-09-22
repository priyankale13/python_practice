#!/usr/bin/python3

l1=[10, 20, 30, 40, 50]
l2=[100, 200, 300, 400, 500]

for e, e1 in zip(l1 , l2[::-1]):
    print(e,e1) 
