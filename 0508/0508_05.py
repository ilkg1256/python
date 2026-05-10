## Lab: 학생 성적 처리

score_dic = {
    "Kim":[99,83,95],
    "Lee":[68,45,78],
    "Choi":[25,56,69]
}

for Name, Score in score_dic.items():
    print(Name, "의 평균성적=",sum(Score)/len(Score))