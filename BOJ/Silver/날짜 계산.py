arr =  input().split()
E, S, M = int(arr[0]), int(arr[1]), int(arr[2])    
year = 1
Flag=True
while Flag:
    if (year-E)%15==0 and (year-S) %28 ==0 and (year-M)%19 ==0:
        Flag=False
        print(year)
    year+=1