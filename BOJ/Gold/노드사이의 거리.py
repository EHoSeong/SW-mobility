from collections import deque
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, d = map(int,input().split())
    graph[n1].append((n2,d))
    graph[n2].append((n1,d))
    
def bfs(start,find):
    dq = deque()
    dq.append((start,0))
    visit = [False]*(N+1)
    while dq:
        s, d = dq.pop()
        if s == find:
            return d
        for i,j in graph[s]:
            if visit[i] ==False:
                visit[i] = True
                dq.append((i,d+j))
for _ in range(M):
    n1,n2 = map(int,input().split())
    print(bfs(n1,n2))