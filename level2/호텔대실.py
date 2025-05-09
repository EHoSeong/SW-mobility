# // 호텔대실
def solution(book_time):

    times = sorted([(toMinute(start),toMinute(end)+10) for start, end in book_time])

    rooms=[]
    for s, e in times:
        for i in range(len(rooms)):
            if rooms[i]<=s:
                rooms[i] = e
                break
        else:
            rooms.append(e)
             
        rooms.sort()


    
    return len(rooms)


def toMinute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m


book_time = [
    ["15:00", "17:00"],
    ["16:40", "18:20"],
    ["14:20", "15:20"],
    ["14:10", "19:20"],
    ["18:20", "21:20"],
]
print(solution(book_time))


# for s,e in times:
#         for i in range(len(rooms)):
#             if rooms[i]<= s:
#                 rooms[i] = e
#                 break
#         else:
#             rooms.append(e)
#         rooms.sort()