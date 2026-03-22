## Lab: 도박상의 확률

import random

Before = 50
Goal = 250
Win = 0

for i in range(100):
    Cash = Before
    while Cash > 0 and Cash < Goal:
        Number = random.randint(1, 2)
        if Number == 1:
            Cash = Cash + 1
        else:
            Cash = Cash - 1
    if Cash == Goal:
        Win = Win + 1

print(f"초기금액 ${Before}")
print(f"목표 금액 ${Goal}")
print(f"100번 중에서 {Win}번 성공.")