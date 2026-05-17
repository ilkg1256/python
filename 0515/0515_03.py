## Lab: 자동차 클래스 작성

class Car:
    def __init__(self, Speed, Color, Model):
        self.Speed = Speed
        self.Color = Color
        self.Model = Model

    def Drive(self):
        self.Speed = 60
    
Car1 = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", Car1.Speed)
print("자동차의 색상은", Car1.Color)
print("자동차의 모델은", Car1.Model)

Car1.Drive
print("자동차의 속도는", Car1.Speed)