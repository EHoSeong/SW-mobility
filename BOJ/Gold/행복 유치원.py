N,K = map(int,input().split())
people = list(map(int,input().split()))
people.sort()
diff = []
for i in range(N-1):
    diff.append(people[i+1]-people[i])
diff.sort()
answer = sum(diff[:N-K])  
print(answer)  