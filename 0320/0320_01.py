## Lab: 산술 퀴즈 프로그램
import random

A = random.randint(1,100)
B = random.randint(1,100)

answer = int(input(f"{A} + {B} = "))
print(answer == A + B)