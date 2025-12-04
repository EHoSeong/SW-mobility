from collections import deque

n = int(input())
ans = 0
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))
cnt = [[1e9] * n for _ in range(n)]
dq = deque()
dq.append((0, 0))
cnt[0][0] = 0
while dq:
    x, y = dq.popleft()
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 1:
                if cnt[nx][ny] > cnt[x][y]:
                    cnt[nx][ny] = cnt[x][y]
                    dq.appendleft((nx, ny))
            elif maps[nx][ny] == 0:
                if cnt[nx][ny] > cnt[x][y] + 1:
                    cnt[nx][ny] = cnt[x][y] + 1
                    dq.append((nx, ny))
print(cnt[n - 1][n - 1])
