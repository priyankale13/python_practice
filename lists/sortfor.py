#!/usr/bin/python3
# method 1 selection sort
ls=[-1,4,6,9,3,1,0,56,8]
print(ls)
for i in range(len(ls)-1):   # iterste through each elemen
    min=i
    for j in range(i+1,len(ls)): #iterate  to comaparision , at the end of loop, last element is sorted.
        if ls[min]>ls[j]:  #finding min elemt
            min=j 
    ls[i],ls[min]=ls[min],ls[i]   # swaping to place in is pos
print(ls)

# method 2 bubble sort

#l1=[0.23,9,56,-2,45]
#print(l1)
#for i in range(len(ls)-1):
 #   for j in range(0,len(ls)-1-i)
