import heapq
V, E = map(int,input().split())
road =[[1e7]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, l = map(int,input().split())
    road[a][b]=l

for k in range(1,V+1):
    for j in range(1,V+1):
        for i in range(1,V+1):
            if road[j][k] ==1e7:
                continue
            if road[j][i] > road[j][k] + road[k][i]:
                road[j][i] =  road[j][k] + road[k][i]

answer = 1e7
for i in range(1,V+1):
    answer = min(answer,road[i][i])
if answer==1e7:
    print(-1)
else:
    print(answer)