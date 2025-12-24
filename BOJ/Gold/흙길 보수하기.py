N, L = map(int, input().split())
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))
water.sort(key=lambda x: x[0])

paper = []
answer = 0
cur = 0

for s, e in water:
    while e > cur:
        if cur>s:
            cur = cur+L
        else:
            cur = s + L
        answer += 1

print(answer)
