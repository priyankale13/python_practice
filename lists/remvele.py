#!/usr/bin/python3

l1=['green','red','black','white','grey','navy','olive']
print("original list:",l1)

#using remove()
l1.remove('red')
print("after removel of 'red' from list using remove('red'):",l1)

#using pop(i) where i is index
l1.pop(2)
print("after removal of ith elemet using pop(i):",l1)

#using del statement
del l1[4]
print("list , using del statement, removed 4th element:",l1)

#using discard, list to set, discard then set to list

l1=set(l1) 
l1.discard('navy')
print("list after removal of 'navy' using discard():",l1)
