## Lab: 소수 찾기

Primes = 50
Num = 2
Count = 0

while Count < Primes:
    Divideto = 2
    Prime = True
    while Divideto < Num:
        if Num % Divideto == 0:
            Prime = False
            break
        Divideto += 1
    if Prime:
        Count += 1
        print(Num, end=" ")
    Num += 1