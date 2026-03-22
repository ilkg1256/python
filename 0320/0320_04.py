## Lab: 물의 상태 출력하기

Temp = int(input("온도를 입력하시오: "))
if Temp <= 0:
    print("물의 상태는 고체입니다.")
elif Temp >= 100:
    print("물의 상태는 기체입니다.")
else:
    print("물의 상태는 액체입니다.")