#!/usr/bin/python3

num=input("enter an integer:")
lst=list(num)
d=dict()
for n in num: 
    d[n]=d.get(n,0)+1
print(d)
lst.sort(key=None,reverse=True)
print(lst)
maxnum=''.join(lst)
print(maxnum)
l1=[]
l2=[]
for i in range(1,int(maxnum)+1):
    if i%2==1:
        l1.append(str(i))
print(l1)


