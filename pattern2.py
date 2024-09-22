#!/usr/bin/python3

n=int(input("Enter odd number < 9 :"))
sp=n//2
st=1
for line_no in range(n//2+1):
    print(" "*sp,"*"*st,sep="")
    sp=sp-1
    st=st+2

sp=1
st=n//2+1
for line_no in range(n//2):
    print(" "*sp,"*"*st,sep="")
    sp=sp+1
    st=st-2
