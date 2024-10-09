def concatstr(s1,s2):
    m1=int(len(s1)/2)
    m2=int(len(s2)/2)
    s3=s1[0]+s2[0]+s1[m1]+s2[m2]+s1[-1]+s2[-1]
    return s3

str1=input("Enter a string:")
str2=input("enter another string:")

print(concatstr(str1,str2))


