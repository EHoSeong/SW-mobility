from bisect import bisect_left
N = int(input())
line = list(map(int,input().split()))
res=[]
answer=0
for i in range(N):
    if i ==0:
        res.append(line[i])
    if res[-1] <line[i]:
        res.append(line[i])
    else:
        x = bisect_left(res,line[i])
        res[x] = line[i]
print(N-len(res))