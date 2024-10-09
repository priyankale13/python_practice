s="This is a good number 9089786756 and 8900000000 is a desired number "
s1="my number is 9130690936,9552310615,0000000000,9999999999"
def checknumber(str1):
    count=0
    m=''
    for char in str1:
        if char.isdigit():
            m=m+char
            #print(m)
        if len(m)==10:
            print(m,end=',')
            m=''
    print(sep='')

checknumber(s)
checknumber(s1)
