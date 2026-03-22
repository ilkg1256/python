## Lab: 파이 계산하기

Divisor = 1.0
Divident = 4.0
Sum = 0.0
Loop_count = int(input("반복횟수:"))

while Loop_count > 0:
    Sum = Sum + Divident / Divisor
    Divident = -1.0 * Divident
    Divisor = Divisor + 2
    Loop_count = Loop_count - 1

print(f"Pi = {Sum}")