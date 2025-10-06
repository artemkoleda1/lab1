x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
    print("WHITE" if (x1 + y1) % 2 == 0 else "BLACK")
else:
    print("NO")