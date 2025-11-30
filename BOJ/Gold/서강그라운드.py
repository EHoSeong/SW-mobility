import heapq
n,m,r = map(int,input().split())

t = list(map(int,input().split()))
answer=0
road = [[]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    road[a].append((b,l))
    road[b].append((a,l))
    
for i in range(1,n+1):
    q = []
    visit=set()
    range=0
    heapq.heappush(q,(i,range))
    item = t[i-1]
    visit.add(i)
    while q:
        cur,currange = heapq.heappop(q)
        for j,l in road[cur]:
            if currange+l <=m and j not in visit:
                visit.add(j)
                item+=t[j-1]
                heapq.heappush(q,(j,currange+l))
    answer = max(item,answer)
print(answer)