d={2:'simran',13:'arpita',16:'aditi',14:'vivek',9:'priyanka',}
vo=['a','o','u','i','e']
def isperfectsq(key):
    for i in range(1,key):
        if key/i==i:
            return 1
def isprime(key):
    if key==2:
        return 1
    if key!=2 and key%2==0:
        return 0
    for i in range(3,int(key/2)):
        if key%i==0:
            return 0
            break
    else:
        return 1

def isodd(key):
    if key%2==1:
        return 1

def empid_name(d):
    for key,val in d.items():
        if isperfectsq(key):
            print(f"{key=} is perfect sqaure and vowels in name:")
            for char in val:
                if char in vo:
                    print(char,end='')
        print(sep='') 
        if isprime(key):
            print(f"{key=} is prime and alternate char in name:")
            for i in range(0,len(val),2):
                print(val[i],end='')
        print(sep='')
        if isodd(key):
            print(f"{key=} is odd number,sum of ascii values of name:")
            sum=0
            for char in val:
                sum=sum+ord(char)
            print(sum)
        else:
            print(f"{key=} is neither perfectsq,nor prime and nor oddnumber")
empid_name(d)
