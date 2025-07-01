def dfs(cur, x, y, parent_x, parent_y, path_length):
    global found_cycle, visit

    if found_cycle:
        return

    visit[x][y] = True

    for dx, dy in direction:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == cur:
            if nx == parent_x and ny == parent_y:
                continue

            if visit[nx][ny]:
                if path_length >= 4:
                    found_cycle = True
                    return
            else:
                dfs(cur, nx, ny, x, y, path_length + 1)
                if found_cycle:
                    return


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())

found_cycle = False

for i in range(N):
    for j in range(M):
        visit = [[False for _ in range(M)] for _ in range(N)]

        dfs(arr[i][j], i, j, -1, -1, 1)

        if found_cycle:
            print("Yes")
            exit()

print("No")
