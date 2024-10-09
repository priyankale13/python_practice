str="I am at CDAC. What about you? I am surprised by current weather!"
cn=0
ce=0
cq=0
cw=0
for i in range(len(str)):
    if str[i]=='.':
        if str[i-1].isascii()==True and str[i-1]!=' ' :
            cn+=1
    if str[i]=='?':
        if str[i-1].isascii()==True and str[i-1]!=' ':
            cq+=1
    if str[i]=='!':
        if str[i-1].isascii()==True and str[i-1]!=' ':
            ce+=1
    if str[i]==' ':
        cw+=1

print("word count:",cw+1)
print("normal sentence:",cn)
print("exclaimatory: ",ce)
print("interagative: ",cq) 
