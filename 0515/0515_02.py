## Lab: 원 클래스 정의

import math

class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def getPerimeter(self):
        return math.pi * self.radius * 2

C = Circle(10)

print("원의 면적", C.getArea())
print("원의 둘레", C.getPerimeter())