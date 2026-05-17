## Lab: 클래스 변수

class Dog:
    Breed = "Bulldog"
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    
DogA = Dog("Buduk", 2)
DogB = Dog("Marry", 3)

print(DogA.Breed)
print(DogB.Breed)
print(Dog.Breed)

print(DogA.Name)
print(DogB.Name)