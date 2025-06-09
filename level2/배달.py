import heapq

def solution(N, road, K):

    graph = [[] for _ in range(N + 1)]
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

    dis = [float("inf")] * (N + 1)
    dis[1] = 0

    heap = [(0, 1)]
    cnt = 0

    while len(heap) > 0:
        d, num = heapq.heappop(heap)

        if dis[num] < d:
            continue

        for neighbor, time in graph[num]:
            cost = d + time
            if cost < dis[neighbor]:
                dis[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))
    for i in dis:
        if i<=K:
            cnt+=1
    return cnt


# N = 6
# road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
# K = 4
N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
solution(N, road, K)
