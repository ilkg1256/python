## Lab: 초등생을 위한 산수 문제 발생기

import random

Flag = True

while Flag:
    A = random.randint(1, 100)
    B = random.randint(1, 100)
    Answer = A + B
    User = int(input(f"{A} + {B} = "))
    if User == Answer:
        print("잘했어요!!")
    else:
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
        Flag = False

