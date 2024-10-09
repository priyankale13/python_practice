s1={10,20,30,40,50}
s2={30,40,50,60,70}
def unionset(s1,s2):
    s3=s1.union(s2)
    return s3
def updateset(s1,s2):
    s1.update(s2)
    return s1
def eitherset(s1,s2):
    s3=set()
    for e1 in s1:
        if e1 in s2:
            s3.add(e1)
    return s3

print("set 1: ",s1)
print("set 2: ",s2)
"""
print("set after joining using union(), : ",unionset(s1,s2)
print("set after joining using update(): ",updateset(s1,s2))
"""
print("set of elements in either set1 or set2: ",eitherset(s1,s2))

