import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = []
right_arr =[]
left_arr = []
for i in range(N):
    num=int(input())
    if len(right_arr) == len(left_arr):
        heapq.heappush(right_arr,num)
    else:
        heapq.heappush(left_arr,-num)
    if left_arr and -left_arr[0]>right_arr[0]:
        right_min = heapq.heappop(right_arr)
        left_max = -heapq.heappop(left_arr)

        heapq.heappush(left_arr,-right_min) 
        heapq.heappush(right_arr,left_max)
    if len(right_arr)>len(left_arr):
        print(right_arr[0])
    else:
        print(-left_arr[0])
        
        