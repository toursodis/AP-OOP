class Calculator:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        return a/b
a=calculator = Calculator()
b=calculator.add(10, 5) 
c=calculator.subtract(10, 5)
d=calculator.multiply(10, 5) 
e=calculator.divide(10, 5) 
print(a)
print(b)
print(c)
print(d)
print(e)