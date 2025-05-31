def solution(dirs):
    directions = {'U': [0,1], 'D': [0,-1], 'L': [-1,0], 'R': [1,0]}
    x, y, path= 0, 0, set()
    for d in dirs:
        dx = x + directions[d][0]
        dy = y + directions[d][1]

        if -5<= dx <=5 and -5<=dy<=5:
            path.add((x,y,dx,dy))
            path.add((dx,dy,x,y))
            x,y  = dx,dy

    return len(path)/2



dirs = "ULURRDLLU"
# dirs = "LULLLLLLU"
print(solution(dirs))
