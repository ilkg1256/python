## Lab: 친구 관리 프로그램

Menu = 0
Friendlist = []

def Plus():
    Name = input("이름을 입력하시오: ")
    Friendlist.append(Name)

def Minus():
    Del = input("삭제하고 싶은 이름을 입력하시오: ")
    if Del in Friendlist:
        Friendlist.remove(Del)
    else:
        print("이름이 발견되지 않았음")

def Changer():
    Old = input("변경하고 싶은 이름을 입력하시요: ")
    if Old in Friendlist:
        Index = Friendlist.index(Old)
        New = input("새로운 이름을 입력하시오: ")
        Friendlist[Index] = New
    else:
        print("이름이 발견되지 않음")


while True:
    print("-"*12)
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    Menu = int(input("메뉴를 선택하시오"))
    if Menu == 1:
        print(Friendlist)
    elif Menu == 2:
        Plus()
    elif Menu == 3:
        Minus()
    elif Menu == 4:
        Changer()
    elif Menu == 9:
        break
    else:
        print("다시 입력해 주세요.")

