def solution(id_list, report, k):
    name_set = [set() for _ in range(len(id_list))]
    id = {}

    call = [0] * len(id_list)
    for i in range(len(id_list)):
        id[id_list[i]] = i

    for i in report:
        id1, id2 = i.split()
        name_set[id[id2]].add(id[id1])

    for i in range(len(name_set)):
        if len(name_set[i]) >= k:
            for x in name_set[i]:
                call[x] += 1
    print(call)
    return call


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
solution(id_list, report, k)

# x = [set()for _ in range(5)]
# print(x)
# x[0]= '3'
# print(x)
# x[2].add('56')
# print(x)
