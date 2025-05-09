# // 무인도 여행
def solution(maps):
    answer = []
    rows, cols = len(maps), len(maps[0])
    grid = [list(row) for row in maps]
    print(grid)
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != "X":
                answer.append(bfs(i, j, grid))
                maps = grid
    answer = sorted(answer, reverse=False)
    if len(answer) == 0:
        answer.append(-1)
    return answer


# // food 들고가지말고 visited로 해보기
def bfs(x, y, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(x, y)]
    food = 0

    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            if grid[x][y] != "X":
                nx, ny = x, y
            else:
                nx = x + dx
                ny = y + dy
            if (
                0 <= nx < len(maps)
                and 0 <= ny < len(maps[0])
                and not (grid[nx][ny] == "X")
            ):
                food += int(grid[nx][ny])
                grid[nx][ny] = "X"
                queue.append((nx, ny))
    return food


# maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
maps = ["XXX","XXX","XXX"]
print(solution(maps))
