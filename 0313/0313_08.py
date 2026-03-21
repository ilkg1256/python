## Lab: 자동판매기 프로그램
Price = int(input("물건값을 입력하시오: "))
Bill = int(input("1000원 지폐개수: "))
Coin500 = int(input("500원 동전개수: "))
Coin100 = int(input("100원 동전개수: "))

change = Bill * 1000 + Coin500 * 500 + Coin100 * 100 - Price

reCoin500 = change//500
change = change%500

reCoin100 = change//100
change = change%100

reCoin10 = change//10
change = change%10

reCoin1 = change

print("500원=", reCoin500, "100원=", reCoin100, "10원=", reCoin10, "1원=", reCoin1)