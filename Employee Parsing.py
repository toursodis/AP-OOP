class Employee:
    def __init__(self,fn,ln,salary):
        self.first_name=fn
        self.last_name=ln
        self.salary=salary
    @staticmethod
    def from_string(string):
        a,b,c=string.split("-")
        return Employee(a,b,c)
emp2 = Employee.from_string("John-Smith-55000")
print(emp2.last_name)