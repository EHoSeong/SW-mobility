from collections import deque

def bfs(node, graph, visited):
    cnt = 0
    dq = deque()
    dq.append(node)
    visited[node] = True
    while len(dq)>0:
        x = dq.popleft()
        cnt+=1
        for g in graph[x]:
            if visited[g] ==False:
                visited[g] = True
                dq.append(g)
    return cnt

def solution(n, wires):
    min_difference = float('inf')
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        visit = [False]*(n+1)
        for j,(a,b) in enumerate(wires):
            if i==j:
                continue
            graph[a].append(b)
            graph[b].append(a)
        first_con = bfs(1,graph,visit)
        second_con= n-first_con
        
        min_difference = min(abs(second_con-first_con),min_difference)


    return min_difference
n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

print(solution(n,wires))