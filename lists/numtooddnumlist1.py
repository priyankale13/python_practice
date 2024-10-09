#!/usr/bin/python3
from itertools import combinations_with_replacement
n=str(3214)
 
l1=list(combinations_with_replacement(n,1))
l2=list(combinations_with_replacement(n,2))
l3=list(combinations_with_replacement(n,3))

l=l1+l2+l3

print(l)

