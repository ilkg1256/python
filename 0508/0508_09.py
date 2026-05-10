## Lab: 이메일 주소 분석

Mailaddress = input("이메일 주소를 입력하시오: ")
Mailid, domain = Mailaddress.split("@")


print(Mailaddress)
print("아이디:", Mailid)
print("도메인:", domain)