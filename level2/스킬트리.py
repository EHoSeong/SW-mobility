def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        cnt = 0
        for i in range(len(tree)):
            if tree[i] in skill:
                if tree[i] == skill[cnt]:
                    cnt += 1
                else:
                    break
        else:
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
