N,K = map(int,input().split())
arr =input()
answer =[]
stack=[]
cnt = 0
target = 0
for a in arr:
    while stack and stack[-1] <a and K>0:
        stack.pop()
        K-=1
    stack.append(a)
if K>0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))