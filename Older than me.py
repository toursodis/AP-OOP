class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def compare_age(self,anotherperson):
        if self.age>anotherperson.age:
            return f"{anotherperson.name} is younger than me."
        elif self.age==anotherperson.age:
            return f"{anotherperson.name} is the same age as me."
        else:
            return f"{anotherperson.name} is older than me."
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))