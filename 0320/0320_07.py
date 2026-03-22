## Lab: 8 매직볼
import random

print("행운의 매직볼로 운세를 출력합니다.")
Answers = random.randint(1,8)
if Answers == 1:
    print("확실히 이루어집니다.")
elif Answers == 2:
    print("좋아 보이네요.")
elif Answers == 3:
    print("믿으셔도 됩니다.")
elif Answers == 4:
    print("저의 생각에는 No입니다.")
else:
    print("다시 질문해주세요.")
