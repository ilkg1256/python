## Lab: BMI 계산하기
Weight = float(input("몸무게를 kg 단위로 입력하시오: "))
Height = float(input("키를 미터 단위로 입력하시오: "))

BMI = Weight / (Height ** 2)
print("당신의 BMI= ", BMI)