ans = []
s=0
for _ in range(9):
    ans.append(int(input()))
ans.sort(reverse=False)
for i in range(0,len(ans)):
    if s==100:
        break
    s = sum(ans)
    s -=ans[i]
    
    for j in range(i+1,len(ans)):
        if s-ans[j] ==100:
            s-= ans[j]
            ans.pop(j)
            ans.pop(i)
            break
for i in range(len(ans)):
    print(ans[i])



