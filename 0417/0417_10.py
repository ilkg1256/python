## Lab: 피타고라스 삼각형

Triangles = []

for X in range(1, 30):
    for Y in range(X, 30):
        for Z in range(Y, 30):
            if X ** 2 + Y ** 2 == Z ** 2:
                Triangles.append(f"({X}, {Y}, {Z})")

print(Triangles)