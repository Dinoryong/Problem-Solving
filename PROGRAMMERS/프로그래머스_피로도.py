''' 20201.11.04
[[80,20].[50,40],[30,10]]

'''
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons, len(dungeons)))
    for case in cases:
        hp, count = k, 0
        for need, consume in case:
            if hp >= need:
                hp -= consume
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer