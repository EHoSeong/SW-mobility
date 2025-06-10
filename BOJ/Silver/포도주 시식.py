N = int(input())
dp = [0]*N
grape = []
for _ in range(N):
    grape.append(int(input()))
dp[0] = grape[0]
if N>1:
    dp[1] = grape[0]+grape[1]
if N>2:
    dp[2] = max(grape[0]+grape[2],grape[1]+grape[2],dp[1])

for i in range(3,N):
    dp[i] = max(dp[i-1],dp[i-3]+grape[i-1]+grape[i],dp[i-2]+grape[i])
print(dp[N-1])
