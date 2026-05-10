## Lab: 머리 글자어 만들기

Sentence = input("문자열을 입력하시오:")

Acronym = " "

for i in Sentence.upper().split():
    Acronym += i[0]

print(Acronym)