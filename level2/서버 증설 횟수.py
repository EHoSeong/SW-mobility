# // 서버 증설 횟수
def solution(players, m, k):
    answer = 0
    server = [m-1 for i in range(24)]
    for idx , p in enumerate(players):
        cnt =0
        if server[idx]<p:
            if (p-server[idx]) % m ==0:
                cnt = (p-server[idx]) //m 
            else:
                cnt = (p-server[idx]) //m  +1
            answer +=cnt
            for i in range(idx, idx+k):
                if i>=len(server):
                    break
                else:
                    server[i]+= cnt*m

    return answer

players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
m =1
k=1
print(solution(players,m,k))