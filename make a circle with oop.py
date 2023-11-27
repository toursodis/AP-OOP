import math
class Circle:
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        return (math.pi*self.radius*self.radius)
    def getPerimeter(self):
        return(2*math.pi*self.radius)
circle=Circle(3)
s=circle.getArea()
a=circle.getPerimeter()
print(s)
print(a)
    
        