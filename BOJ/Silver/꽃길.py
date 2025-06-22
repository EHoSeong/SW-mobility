garden = []
visit = []

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 10001


def check(x, y, visit):
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if (nx, ny) in visit:
            return False
    return True


def dfs(visit, total):
    global answer
    if total >= answer:
        return
    if len(visit) == 15:
        answer = min(answer, total)

    else:
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if check(i, j, visit) and (i, j) not in visit:
                    flower = [(i, j)]
                    # visit.append((i, j))
                    flower_total = garden[i][j]
                    for dx, dy in direction:
                        nx = i + dx
                        ny = j + dy
                        flower_total += garden[nx][ny]
                        flower.append((nx, ny))
                    dfs(visit + flower, total + flower_total)


N = int(input())
for _ in range(N):
    garden.append(list(map(int, input().split())))

dfs([], 0)
print(answer)
