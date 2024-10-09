#!/usr/bin/python3

l1=[5,6,7]
l2=[0,1]
print("original list1:",l1)
print("original lis2:",l2)
res=[str(i)+str(j) for i in l1 for j in l2]
print("resultant list after concatenation:",res)
#concat every element of l1 with every element of l2
