def solution(storey):
    answer = 0
    while storey > 0:
        rest = storey % 10
        storey = storey // 10
        if rest > 5 or (storey%10 >=5 and rest ==5):
            answer += 10 - rest
            storey += 1
        else:
            answer += rest

    return answer


storey = 65
print(solution(storey))
