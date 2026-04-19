## Lab: 성적 처리 프로그램

Students = 5
Scorelist = []
Counts_80 = 0

for i in range(Students):
    Value = int(input("성적을 입력하세요:"))
    Scorelist.append(Value)

print("성적 평균= ", sum(Scorelist)/Students)
print("최대점수= ", max(Scorelist))
print("최소점수= ", min(Scorelist))

for score in Scorelist:
    if score >= 80:
        Counts_80 += 1

print("80점 이상=", Counts_80)