class Employee:
    coname='Myntra'
    def __init__(self):
        self.empno=int(input("Enter employee no:"))
        self.name=input("Enter employee name:")
        self.deptno=int(input("Enter deptno:"))
        self.mgr=int(input("enter mgr no:"))
    def display_emp(self):
        print(self.empno,self.name,self.deptno,self.mgr)
    @classmethod
    def display_coname(cls):
        print(cls.coname)
    @staticmethod
    def display_comp():
        print(Employee.coname)

e1=Employee()
e1.display_emp()
e1.display_coname()
e1.display_comp()

e2=Employee()
e2.display_emp()
e2.display_coname()
e2.display_comp()
