def solution(a):
    if len(a) < 4:
        answer = 3
    else:
        n = len(a)
        answer = 2
        left_min = [0] * n
        left_min[0] = a[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], a[i])

        right_min = [0] *n
        right_min[n-1] = a[n-1]
        for i in range(n-2, -1,-1):
            right_min[i] = min(right_min[i+1], a[i])

        for i in range(1, len(a) - 1):
            leftmin = left_min[i-1]
            rightmin = right_min[i+1]
            if (
                leftmin < a[i] < rightmin
                or rightmin < a[i] < leftmin
                or min(leftmin, rightmin, a[i]) == a[i]
            ):
                answer += 1
    # print(answer)
    return answer


a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
solution(a)
