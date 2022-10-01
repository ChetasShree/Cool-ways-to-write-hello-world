def halfDiamondStar(N):
    for i in range(N-1):
        for j in range(0, i + 1):
            print("*", end="")
        print()

    print("Hello World")
    for i in range(1, N):
        for j in range(i, N):
            print("*", end="")
        print()


N = 5
halfDiamondStar(N)
