#!/usr/bin/python3

l1=['hello','priyanka','arpita','as','reshma',[12,1,'hi']]
l2=[]
def countleng(n):
    count=0
    for e in l1:
        if len(e)>n:
            count+=1
            l2.append(e)
    return count,l2


num=int(input("enter a number:"))
print(f"no of words having length more than{num}={countleng(num)}")

#doesnt work for int values
