from collections import deque
N,M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int,input())))

def bfs():
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append((0,0,0))
    visit[0][0][0] = 1
    while dq:
        x,y,w = dq.popleft()
        if x ==N-1 and y ==M-1:
            return visit[x][y][w] 
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny] ==False and visit[nx][ny][w]==0:
                    visit[nx][ny][w]= visit[x][y][w]+1
                    dq.append((nx,ny,w))
                elif maps[nx][ny] ==True and w ==0:
                    visit[nx][ny][w+1] == visit[x][y][w]+1
                    dq.append((nx,ny,w+1))
    return -1
        
print(bfs())