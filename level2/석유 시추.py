from collections import deque


def solution(land):
    vis = [[False] * len(land[0]) for _ in range(len(land))]
    # 붙어있는 땅의 사이즈로 realLand를 재설정
    realLand = [[0] * len(land[0]) for _ in range(len(land))]

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and vis[i][j] == False:
                dq = deque()
                dq.append((i, j))
                vis[i][j] = True
                # 붙어있는 부분 담을 lan 배열열
                lan = []
                lan.append((i,j))
                # 붙어있는 땅의 size
                size= 0
                while len(dq) > 0:
                    size+=1
                    x, y = dq.popleft()
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if (
                            0 <= nx < len(land)
                            and 0 <= ny < len(land[0])
                            and vis[nx][ny] == False
                            and land[nx][ny] == 1
                        ):
                            vis[nx][ny] = True
                            dq.append((nx, ny))
                            lan.append((nx, ny))
                # 붙어 있는 땅의 값을 size로 바꾼다.
                for xx, yy in lan:
                    realLand[xx][yy] = size

    answer = []
    # 땅의 사이즈로 그린 realLand에서 land[0] 길이만큼 순서대로 찔렀을떄의 각 합을 구하는 공식
    for i in range(0,len(land[0])):
        sum = 0
        pre = 0
        for j in range(len(land)):
            pre = realLand[j-1][i]
            if realLand[j][i] !=0 and pre != realLand[j][i]:
                sum+= realLand[j][i]
        answer.append(sum)
    if len(answer) ==0:
        return 0
    return max(answer)


# land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
# land = [[1,1,1,1,1],[1,0,0,0,0],[1,0,0,1,0], [1,0,0,0,0], [1,1,1,1,1]]
land = [[1,1,1,1], [1,0,0,0],[1,0,1,0],[1,0,0,0],[1,1,1,1]]
# land = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0]]
print(solution(land))
