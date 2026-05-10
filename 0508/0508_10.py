## Lab: 문자열 분석

Sentence = input("문자열을 입력하시오: ")

Analyze = {"alphas":0, "digits":0, "spaces":0}

for i in Sentence:
    if i.isalpha():
        Analyze["alphas"] += 1
    if i.isdigit():
        Analyze["digits"] += 1
    if i.isspace():
        Analyze["spaces"] += 1


print(Analyze)