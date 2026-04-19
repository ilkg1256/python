## Lab: 리스트 함축 사용하기

Numberlist = [i for i in range(100) if i % 2==0 and i % 3==0]

print(Numberlist)

### 도전 문제

Numberlist2 = [i for i in range(10)]
Numberlist2 = ["짝수" if i % 2 == 0 else "홀수" for i in Numberlist2]
print(Numberlist2)