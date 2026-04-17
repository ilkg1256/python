## Lab: 주급 계산 프로그램

def weeklyPay(rate, hour):
    Money = 0
    if hour>30:
        Money = rate * 30 + 1.5 * rate * (hour - 30)
    else:
        Money = rate * hour
    return Money

Rate = int(input("시급을 입력하시오:"))
Times = int(input("근무 시간을 입력하시오:"))
print(weeklyPay(Rate,Times)) 