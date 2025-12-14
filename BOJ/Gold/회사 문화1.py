n, m = map(int, input().split())

coms = [0] * (n + 1)
nums = [0] + list(map(int, input().split()))
for _ in range(m):
    a, c = map(int, input().split())
    coms[a] += c
for i in range(2, n + 1):
    coms[i] += coms[nums[i]]
for i in range(1, n + 1):
    print(coms[i], end=" ")
