from collections import deque

N, M = map(int, input().split())
bridge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    bridge[a].append((b, w))
    bridge[b].append((a, w))
start, end = map(int, input().split())


def bfs(weight):
    dq = deque()
    dq.append(start)
    visit = set()
    visit.add(start)
    while dq:
        x = dq.popleft()
        if x == end:
            return True
        for i,w in bridge[x]:
            if i not in visit and w >=weight:
                visit.add(i)
                dq.append(i)
    return False
        
s,e = 1,1000000000
answer = 0
while s<=e:
    mid = (s+e)//2
    if bfs(mid):
        answer= mid
        s = mid +1
    else:
        e = mid-1
        

print(answer)
