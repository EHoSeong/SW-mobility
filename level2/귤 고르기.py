def solution(k, tangerine):
    tangerine_dict = {}
    for i in tangerine:
        tangerine_dict[i] = tangerine_dict.get(i, 0) + 1
    answer = 0
    tangerine_dict = sorted(
        tangerine_dict.items(), key=lambda item: item[1], reverse=True
    )
    for index, d in enumerate(tangerine_dict):
        if k==0:
            break
        if tangerine_dict[index][1] <= k:
            k -= tangerine_dict[index][1]
            answer += 1
        elif tangerine_dict[index][1] > k:
            answer += 1
            break
    return answer


k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

# k =2
# tangerine=[1, 1, 1, 1, 2, 2, 2, 3]

print(solution(k, tangerine))
