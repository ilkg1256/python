## Lab: Tic-Tac-Toe

Board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

X = 0
Y = 0

def Draw():
    for i in range(3):
        for j in range(3):
            print(" " + Board[i][j] + "| ", end = " ")
        print(" ", end="\n")
        if (i != 2):
            print("---|---|---")

def Player():
    X = int(input("다음 수의 x좌표를 입력하세요: "))
    Y = int(input("다음 수의 y좌표를 입력하시오: "))
    if Board[Y-1][X-1] != " ":
        print("잘못된 위치입니다.")
        Player()
    else:
        Board[Y-1][X-1] = "×"

def PC():
    Done = False
    for i in range(3):
        for j in range(3):
            if Board[i][j] == " " and not Done:
                Board[i][j] = "○"
                Done = True
                break

while True:
    Draw()
    Player()
    PC()


