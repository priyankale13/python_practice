str1="AaaBCDEFGHIJKLMNOPQRSTUVWXYZ"
length=len(str1)
rem=length%4
rng=length//4
for i in range(0,rng*4,4):
    for j in range(4):
        print(str1[i+j],end='')
    print(sep='')    
for i in range(rng+1,length):
    print(str1[i],end='')
