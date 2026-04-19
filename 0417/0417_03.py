## Lab: 콘테스트 평가

Scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거 전 ", Scores)

Scores.remove(max(Scores))
Scores.remove(min(Scores))

print("제거 후 ", Scores)