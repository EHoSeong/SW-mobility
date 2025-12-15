N, M = map(int, input().split())
arr = list(map(int, input().split()))


def divide(target):
    min_value = arr[0]
    max_value = arr[0]
    cnt = 1
    for num in arr:
        cur_max = max(max_value, num)
        cur_min = min(min_value, num)
        if cur_max - cur_min > target:
            cnt += 1
            min_value = num
            max_value = num
        else:
            min_value = cur_min
            max_value = cur_max
    if cnt <= M:
        return 1
    return 0


start = 0
end = max(arr)
answer = 0
while start <= end:
    mid = (start + end) // 2
    if divide(mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)
