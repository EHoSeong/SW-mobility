# //미로탈출 bfs
def solution(maps):
    start, lever, exit = None, None, None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                exit = (i, j)

    toLever = bfs(start, lever, maps)
    if toLever == -1:
        return -1
    toExit = bfs(lever, exit, maps)
    if toExit == -1:
        return -1
    return toLever + toExit


def bfs(start, target, maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(start[0], start[1], 0)]
    while queue:
        x, y, dist = queue.pop(0)
        if (x, y) == target:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and maps[nx][ny] != "X"
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1


# maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
# maps = ["SOOOL", "OXXXO", "OOOOO", "OXXXX", "OOOOE"]
maps = ["SOOOO", "OOOOO", "OLOOE", "OOOOO", "OOOOO"]
print(solution(maps))