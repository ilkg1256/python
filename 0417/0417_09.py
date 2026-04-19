## Lab: 누적값 리스트 만들기

Originlist = [10, 20, 30, 40, 50]

NewList = [sum(Originlist[0:i+1]) for i in range(0, len(Originlist))]

print("원래 리스트: ", Originlist)
print("새로운 리스트: ", NewList)