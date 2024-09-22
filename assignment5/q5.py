#!/usr/bin/python3

l1=["1231","qwewr","zxcz","we","a","1221","mnbcfom"]
count=0
for e in l1:
    if len(e)>2:
        if e[0]==e[-1]:
            count=count+1

print(count)
