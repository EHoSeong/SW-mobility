import heapq
N = int(input())
course = []
q=[]
for _ in range(N):
    s,e = map(int,input().split())
    course.append((s,e))
course.sort()
heapq.heappush(q,course[0][1])
for i in range(1,N):
    start, end = course[i]
    if start < q[0]:
        heapq.heappush(q,end)
    else:
        heapq.heappop(q)
        heapq.heappush(q,end)
print(len(q))