## Lab: 사용자 입력 검증하기

print("="*10)
print('''
메뉴 1번: 치즈 버거
메뉴 2번: 치킨 버거
메뉴 3번: 불고기 버거
      ''')
print("="*10)
Order = int(input("메뉴를 선택하세요: "))

if Order >= 1 and Order <= 3:
    print("메뉴", Order)
else:
    print("잘못 입력하셨습니다.")