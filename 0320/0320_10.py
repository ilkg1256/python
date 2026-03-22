## Lab: 올바른 삼각형 구분

A = int(input("삼각형의 한 변을 입력하시오: "))
B = int(input("삼각형의 한 변을 입력하시오: "))
C = int(input("삼각형의 한 변을 입력하시오: "))

if (A + B) > C and (B + C) > A and (A + C) > B:
    print("올바른 삼각형")
else:
    print("올바르지 않은 삼각형")