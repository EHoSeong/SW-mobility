# // 숫자 변환하기   *2  *3 +n  greedy 유형


def solution(x, y, n):
    answer = bfs(x, y, n, 0)
    return answer


def bfs(curr, target, num, times):
    queue = [(curr, target, num, times)]
    ans = []
    while len(queue) > 0:
        x, y, n, times = queue.pop(0)
        if x * 3 <= y:
            queue.append((x * 3, y, n, times + 1))
        if x * 2 <= y:
            queue.append((x * 2, y, n, times + 1))
        if x + num <= y:
            queue.append((x + n, y, n, times + 1))
        if x == y:
            ans.append(times)
    if len(ans) == 0:
        return -1
    ans = sorted(ans)
    return ans[0]

x = 10
y = 40
n = 30
print(solution(x, y, n))

# def bfs(curr, target, num, times):
#     queue = [(curr, target, num, times)]
#     ans = []
#     while len(queue) > 0:
#         x, y, n, times = queue.pop(0)
#         if x * 3 <= y:
#             queue.append((x * 3, y, n, times + 1))
#         if x * 2 <= y:
#             queue.append((x * 2, y, n, times + 1))
#         if x + num <= y:
#             queue.append((x + n, y, n, times + 1))
#         if x == y:
#             ans.append(times)
#     if len(ans) == 0:
#         return -1
#     ans = sorted(ans)
#     return ans[0]