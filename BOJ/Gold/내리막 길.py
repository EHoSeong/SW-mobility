import sys
sys.setrecursionlimit(10 ** 8)
M,N = map(int,input().split())
maps = []
dp=[[-1]*N for _ in range(M)]

for _ in range(M):
    maps.append(list(map(int,input().split())))

answer=[]

def dfs(x,y):
    if x==M-1 and y ==N-1:
        return 1
    if dp[x][y]!= -1:
        return dp[x][y]
    ways=0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx,dy in directions:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[x][y]:
            ways+= dfs(nx,ny)
    dp[x][y]=ways
    return dp[x][y]
        
    
dfs(0,0)
print(dp[0][0])