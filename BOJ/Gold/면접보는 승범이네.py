import heapq

n, m, k = map(int, input().split())
INF = float("inf")
road = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    road[e].append((s, d))
place = list(map(int, input().split()))

result = [INF] * (n + 1)
h = []
q = []
for p in place:
    result[p] = 0
    heapq.heappush(q, (0, p))
while q:
    cur_d, cur_loc = heapq.heappop(q)
    if result[cur_loc] < cur_d:
        continue
    else:
        for target, dist in road[cur_loc]:
            new_dist = cur_d + dist
            if result[target] >new_dist:
                result[target] = new_dist
                heapq.heappush(q,(new_dist,target))
max_loc = 0
max_dist=-1

for i in range(1,n+1):
    if result[i] != INF:
        if result[i]>max_dist:
            max_loc = i
            max_dist = result[i]
            
print(max_loc)
print(max_dist)