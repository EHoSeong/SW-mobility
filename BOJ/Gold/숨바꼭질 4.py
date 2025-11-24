from collections import deque

N, K = map(int, input().split())
move = [0] * 100001
dist = [0] * 100001
answer = 0
time = 0


def bfs():
    dq = deque()
    dq.append(N)
    dist[N] = 1
    while dq:
        x = dq.popleft()
        if x == K:
            print(dist[x])
            cases(x)
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= 100000 and dist[i] == 0:
                move[i] = x
                dist[i] = dist[x] + 1
                dq.append(i)

def cases(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(" ".join(map(str, arr[::-1])))


bfs()
