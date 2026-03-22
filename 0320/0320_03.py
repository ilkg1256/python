## Lab: 세일 가격 계산

Price = int(input("정가를 입력하시오: "))
if Price >= 100:
    print("10층에서 사은품을 받아가세요.")
    print(f"할인된 가격 = { Price * 0.85 }")
else:
    print(f"할인된 가격 = { Price * 0.9 }")