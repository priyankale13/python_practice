#!/usr/bin/python3

l1=['asap','qwerty','saas','pass','success']

def counts(l):
    
    for e in l:
        cnts=0
        for char in e:
            #print(char)
            if char=='s':
                #print(char)
                cnts+=1
                #print(cnts)
        if cnts==2:
            print(e)

print("list of strings is:",l1)
print("strings conatining s two times:")
counts(l1)

