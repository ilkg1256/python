## Lab: 축구게임

import random

Drawnum = random.randint(1, 3)
User = input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)")
if Drawnum == User:
    print("수비에 성공하셨습니다.")
else:
    print("패널티킥에 성공하였습니다.")