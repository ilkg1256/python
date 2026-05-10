## Lab: 문자열의 공통 분자

Sentence = input("입력 테스트: ")
Words = Sentence.split(" ")

Unique = set(Words)

print("사용된 단어의 개수=", len(Unique))
print(Unique)