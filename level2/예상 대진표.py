def solution(n, a, b):
    cnt = 0
    while b != a:
        cnt += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return cnt
n = 8
a = 4
b = 7

solution(n, a, b)
