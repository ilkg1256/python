## Lab: 로봇 기자 만들기
Stadium = input("경기장은 어디입니까? ")
Winteam = input("이긴 팀은 어디입니까? ")
Loseteam = input("진 팀은 어디입니까? ")
Bestplayer = input("우수선수는 누구입니까?")
Score = input("스코어는 몇대 몇입니까?")

print("="*10)
print(f'''
오늘 {Stadium}에서 야구 경기가 열렸습니다.
{Winteam}과 {Loseteam}는 치열한 공방전을 펼쳤습니다.
{Bestplayer}이 맹활약을 하였습니다.
결국 {Winteam}이 {Loseteam}을 {Score}로 이겼습니다.
''')
print("="*10)