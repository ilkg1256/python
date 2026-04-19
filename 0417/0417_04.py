## Lab: 리스트로 스택 흉내내기

Fakestack = []

for i in range(3):
    Value = input("과일을 입력하시오:")
    Fakestack.append(Value)

for i in range(3):
    print(Fakestack.pop())