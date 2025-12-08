from collections import deque

v, h = map(int, input().split())
maps = []
cnt = 0
for i in range(v):
    maps.append(list(map(int, input().split())))
    cnt += sum(maps[i])


def melted():
    melt = []
    dq = deque()
    dq.append((0, 0))
    visit = set()
    visit.add((0, 0))
    while dq:
        x, y = dq.popleft()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < v and 0 <= ny < h and (nx, ny) not in visit:
                visit.add((nx, ny))
                if maps[nx][ny] == 0:
                    dq.append((nx, ny))
                elif maps[nx][ny] == 1:
                    melt.append((nx, ny))
    for x, y in melt:
        maps[x][y] = 0
    return len(melt)


time = 0
cheese = 0
while True:
    cheese = melted()
    cnt -= cheese
    time += 1
    if cnt == 0:
        break
print(time)
print(cheese)
