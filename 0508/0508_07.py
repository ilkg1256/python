## Lab: 회문 검사하기

Originaltxt = input("문자열을 입력하시오: ")

Reversedtxt = Originaltxt[::-1]

if Originaltxt == Reversedtxt:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")