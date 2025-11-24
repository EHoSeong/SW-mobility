N = int(input())
skill = list(map(int,input().split()))
left, right = 0,N-1
answer = 0

while left+1< right:
    answer = max(answer,(right-left-1)*min(skill[left],skill[right]))
    if skill[left]> skill[right]:
        right-=1
    else:
        left+=1
print(answer)