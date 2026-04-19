## Lab: 전치 행렬 계산

Original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Transposed = []

print("원래 행렬= ", Original)

for i in range(len(Original[0])):
    Transrow = []
    for j in Original:
        Transrow.append(j[i])
    Transposed.append(Transrow)

print("전치 행렬= ", Transposed)