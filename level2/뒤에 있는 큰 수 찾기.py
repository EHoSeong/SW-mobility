# // 뒤에 있는 큰 수 찾기
from collections import deque
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    dq = deque()

    for idx, num in enumerate(numbers):
        while dq and numbers[dq[-1]] < num:
            answer[dq.pop()] = num
        dq.append(idx)
    # for i in range(len(numbers)-1):
    #     if numbers[i+1] > numbers[i]:
    #         answer[i] = numbers[i+1]
    #         while len(dq)>0:
    #             index , val = dq.pop()
    #             if numbers[i+1] > val:
    #                 answer[index] = numbers[i+1]
    #     else:
    #         dq.append((i,numbers[i]))
    return answer

# numbers = [2, 3, 3, 5]
numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))


# def solution(numbers):
#     answer = [-1 for _ in range(len(numbers))]
#     dq = deque()
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[j]>numbers[i]:
#                 answer[i] = numbers[j] 
#                 break
#     return answer