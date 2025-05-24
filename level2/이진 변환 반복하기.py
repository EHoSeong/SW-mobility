def solution(s):
    answer = []
    times = 0
    cnt = 0
    while len(s)>1:
        times+=1
        value = ''
        for i in s:
            if i == '0':
                cnt+=1
            elif i=='1':
                value+=i
        new = ''
        x = len(value)
        while x>0:
            new = str(x%2)+new
            x = x//2
        s = new
    answer.append(times)
    answer.append(cnt)
    return answer

s= "110010101001"
# s = "01110"
# s = "1111111"
print(solution(s))