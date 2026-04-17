## Lab: 구조화 프로그래밍 실습

def Main():
    while True:
        print("1. 섭씨 온도 -> 화씨 온도")
        print("2. 화씨 온도 -> 섭씨 온도")
        print("3. 종료")
        Selection = int(input("메뉴를 선택하세요:"))
        if Selection == 1:
            C_temp = int(input("섭씨 온도를 입력하시오:"))
            print("화씨 온도 =", Celsius(C_temp))
        elif Selection == 2:
            F_temp = int(input("화씨 온도를 입력하시오:"))
            print("섭씨 온도 =", Fahrenheit(F_temp))
        else:
            break
    


def Celsius(c):
    Temp = c * 9.0 / 5.0 + 32
    return Temp

def Fahrenheit(f):
    Temp = (f - 32.0)*5.0/9.0 
    return Temp

Main()