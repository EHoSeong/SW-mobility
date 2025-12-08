import sys
input = sys.stdin.readline
N = int(input())
arr=[]
answer=[]
people=0
for i in range(N):
    num,person = map(int,input().split())
    arr.append((num,person))
    people+= person

arr.sort(key = lambda x:x[0])
p = 0
for v,person in arr:
    p +=person
    if p>=people/2:
        print(v)
        break