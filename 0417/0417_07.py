## Lab: 리스트 변경 함수

def modify(Values, Factor):
    for i in range(len(Values)):
        Values[i] = Values[i] * Factor

Salary = [200, 250, 300, 280, 500]

print("인상 전", Salary)
modify(Salary, 1.3)
print("인상 후", Salary)