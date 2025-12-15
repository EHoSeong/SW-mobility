T = int(input())

answer = 0
for _ in range(T):
    N, M = map(int, input().split())
    bridge = [[] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        f, s, d = map(int, input().split())
        bridge[f].append((s, d))
        bridge[s].append((f, d))
    visit = [False] * (N + 1)

    def dfs(i):
        visit[i] = True
        last = True
        dynamite = 0
        for n, d in bridge[i]:
            if not visit[n]:
                last = False
                dynamite += min(d, dfs(n))
        if last:
            return 1000000
        return dynamite

    if N == 1:
        print(0)
    else:
        print(dfs(1))
print(bridge)