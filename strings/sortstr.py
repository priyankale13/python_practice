def arrangestr(s):
    l=[]
    u=[]
    for char in s:
        if char.islower():
            l.append(char)
        else:
            u.append(char)
    str=''.join(l+u)
    return str

s1=input("enter string in mixed cases:")
print(arrangestr(s1)) 
