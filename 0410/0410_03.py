## Lab: 이분법

def Func(x):
    return(x**2-x-1)

def Bisection(a, b, error):
    if Func(a) * Func(b) > 0:
        print("구간에서 근을 찾을 수 없습니다.")
    else:
        while (b - a)/2.0 > error:
            Midpoint = (a + b)/2.0
            if Func(Midpoint) == 0:
                return(Midpoint)
            elif Func(a) * Func(Midpoint) < 0:
                b = Midpoint
            else:
                a = Midpoint
        return(Midpoint)

Answer = Bisection(1,2,0.0001)

print("x**2-x-1의 근", Answer)