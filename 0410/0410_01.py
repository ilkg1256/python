## Lab: 피자 크기 비교

def Main():
    print("20cm 피자 2개의 면적:", Area(20)*2)
    print("30cm 피자 1개의 면적:", Area(30))

def Area(Radius):
    Area = Radius ** 2 * 3.14
    return Radius

Main()