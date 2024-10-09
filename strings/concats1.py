def concatstr(s1,s2):
    length=len(s1) if len(s1)>len(s2) else len(s2)
    newstr=''
    s2=s2[::-1]
    for i in range(length):
        if i<len(s1):
            newstr+=s1[i]
        if i<len(s2):
            newstr+=s2[i]
    return newstr

str1=input("Enter a string:")
str2=input("Enter another string:")
print(concatstr(str1,str2))
