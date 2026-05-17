## Lab: 벡터 객체에 특수 메소드 정의하기

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, Other):
        return Vector2D(self.x + Other.x, self.y + Other.y)
    
    def __sub__(self, Other):
        return Vector2D(self.x - Other.x, self.y - Other.y)
    
    def __eq__(self, Other):
        return self.x == Other.x and self.y == Other.y
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
U = Vector2D(0, 1)
V = Vector2D(1, 0)
W = Vector2D(1, 1)
A = U + V
print( A)
