# // 숫자 변환하기   *2  *3 +n  greedy 유형
from collections import deque

def solution(x, y, n):

    answer = bfs(x, y, n, 0)
    # answer_dfs = dfs(x, y, n, 0, answer)
    # if len(answer_dfs) == 0:
    #     return -1
    return answer



def bfs(curr, target, num, times):
    dq = deque()
    dq.append((curr,target,num,times))
    while len(dq) > 0:
        x, y, n, times = dq.popleft()
        if x==y:
            return times
        if y%3 ==0 and (y//3)>=x:
            dq.append((x , y//3, n, times + 1))
        if y%2 ==0 and (y//2)>=x:
            dq.append((x , y//2, n, times + 1))
        if (y-n) >=x:
            dq.append((x, y-n, n, times + 1))

    
    return -1


x = 2
y = 5
n = 4
print(solution(x, y, n))

def dfs(curr, target, n, times, answer):
    if len(answer) !=0 and min(answer)<times:
        pass
    if curr == target:
        answer.append(times)
    elif curr < target:
        dfs(curr * 3, target, n, times + 1, answer)
        dfs(curr * 2, target, n, times + 1, answer)
        dfs(curr + n, target, n, times + 1, answer)
    elif curr > target:
        pass
    return answer

