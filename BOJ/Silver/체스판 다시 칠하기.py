N, M = map(int, input().split())
maps = []
result = []
for i in range(N):
    maps.append(input())

for a in range(N - 7):
    for b in range(M - 7):
        case1 = 0
        case2 = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if maps[i][j] == "W":
                        case1 += 1
                    if maps[i][j] == "B":
                        case2 += 1
                else:
                    if maps[i][j] == "B":
                        case1 += 1
                    if maps[i][j] == "W":
                        case2 += 1
        result.append(case1)
        result.append(case2)
print(min(result))
