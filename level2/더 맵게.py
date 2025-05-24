import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1:
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        if x1 >= K:
            return answer
        else:
            answer += 1
            new = x1 + x2 * 2
            heapq.heappush(scoville, new)
    if scoville[0] < K:
        return -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]

k = 7
print(solution(scoville, k))
