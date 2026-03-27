## Lab: 팩토리얼 계산하기

Number = int(input("정수를 입력하시오: "))
Fact = 1
for i in range(1, Number + 1):
    Fact = Fact * i

print(f"{Number}!은 {Fact}이다.")