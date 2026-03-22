## Lab: 방정식의 해 구하기

Count = 100
Start = 1.0
End = 2.0

for i in range(Count):
    X = Start + i * ((End - Start)/Count)
    F = (X ** 2 - X - 1)
    if abs(F-0.0) < 0.01:
        print("방정식의 해는 ",X)