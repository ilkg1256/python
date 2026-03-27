## Lab: 숫자 맞추기 게임

import random

Tried = 0
User = 0
Choose = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

while User != Choose:
    User = int(input("숫자를 입력하시오: "))
    Tried = Tried + 1
    if User < Choose:
        print("너무 낮음!")
    elif User > Choose:
        print("너무 높음!")

if User == Choose:
    print("축하합니다. 시도 회수=", Tried)
else:
    print("정답은", Choose)