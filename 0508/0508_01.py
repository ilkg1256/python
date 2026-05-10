## Lab: 문자열의 공통 문자

Text1 = input("첫 번째 문자열: ")
Text2 = input("두 번째 문자열: ")

Sets = list(set(Text1) & set(Text2))

print("공통적인 글자: ", end=" ")
for i in Sets:
    print(i, end=" ")