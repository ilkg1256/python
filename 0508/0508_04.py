## Lab: 주소록 작성

def Menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    Sel = input("메뉴 항목을 입력하세요: ")
    return Sel

def Contact():
    Name = input("이름: ")
    Number = input("전화번호: ")
    return Name, Number

Address = { }
while True:
    UserInput = Menu()
    if UserInput == "1":
        Name, Number = Contact()
        Address[Name] = Number
    elif UserInput == "2":
        Name, Number = Contact()
        Address.pop(Name)
    elif UserInput == "3":
        ## 도전 문제
        Name = input("이름: ")
        print(Address[Name])
    elif UserInput == "4":
        for i in sorted(Address):
            print(f"{i}의 전화번호: {Address[i]}")
    elif UserInput == "5":
        break
    else:
        continue