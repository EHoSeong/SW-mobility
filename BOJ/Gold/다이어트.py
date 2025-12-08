G = int(input())
a = 1
b = 2
answer = []
while b <= 100000:
    diff = b * b - a * a

    if diff == G:
        answer.append(b)
        b += 1
    elif diff < G:
        b += 1
    else:
        a += 1

if answer:
    for a in answer:
        print(a)
else:
    print(-1)
