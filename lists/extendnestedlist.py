#!/urs/bin/python3
l1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']

l2=['h','i','j']

print("list before extending:",l1)
print("sublist to extend with: ",l2)

l1[2][1][2].extend(l2)

print("list after extending:",l1)


#using insert() and for loop
#i=2
#while i<(len(l2)+2):
#    for e in l2:
#        l1[2][1][2].insert(i,e)
#    i+=1

#print(l1)
