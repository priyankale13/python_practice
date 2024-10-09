class Mylist:
    def __init__(self,ml):
        self.ml=ml
        
    def __add__(self,other):
        if isinstance(other,Mylist)==True:
            ml=self.ml+other.ml
            ml=list(set(ml))
        return Mylist(ml)
    def __sub__(self,other):
        if isinstance(other,Mylist)==True:
            ml=self.ml+other.ml
            dml=dict()
            for e in str(ml):
                dml[e]=dml.get(e,0)+1
            for key,val in list(dml.items()):
                if val>1:
                    dml.pop(key)
            ml=(list(dml))
        return Mylist(ml)
l1=[1,2,3,4,5]
l2=[4,5,6,7]
print("list 1:",l1)
print("list 2:",l2)
print("overriding '+' , adding two list and removing duplicates:")
obl1=Mylist(l1)
obl2=Mylist(l2)
l3=obl1+obl2
print(l3.ml)
print("Overriding '-', adding two list and deleting elements who are repeated:")
l4=obl1-obl2
print(l4.ml)
