from collections import deque

R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(list(input()))
time = 1
dqJ = deque()
dqF = deque()
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    global dqJ
    global time
    size = len(dqJ)
    for _ in range(size):
        x, y = dqJ.popleft()
        if x ==R-1 or x ==0 or y ==0 or y==C-1:
            return time
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0<=nx< R and 0<=ny < C and maps[nx][ny] == ".":
                maps[nx][ny]="J"
                dqJ.append((nx, ny))
    return None
def firebfs(maps):
    global dqF 
    size = len(dqF)
    for _ in range(size):
        x, y = dqF.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if  0<=nx < R and ny >= 0 and ny < C :
                if maps[nx][ny] == "." or maps[nx][ny]=='J':
                    maps[nx][ny] = "F"
                    dqF.append((nx, ny))

for i in range(R):
    for j in range(C):
        if maps[i][j] == "J":
            dqJ.append((i, j))
        elif maps[i][j] == "F":
            dqF.append((i, j))

def solve():
    global time
    while dqJ:
        firebfs(maps)
        result = bfs()
        if result is not None:
            return result
        time += 1
    return "IMPOSSIBLE"
print(solve())
