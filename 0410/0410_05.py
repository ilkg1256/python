## Lab: 여러 개의 값 반환

def Info():
    Name = input("이름:")
    Age = input("나이:")
    return Name, Age

User_name, User_age = Info()
print(f"이름은 {User_name} 이고 나이는 {User_age}살입니다.")