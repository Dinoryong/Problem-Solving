def solution(a, b):
    answer = 0
    c = a**b
    c = str(c)
    answer = c[-1:-6:-1]
    answer = answer[::-1]
    answer = int(answer)
    return answer



1
2
3
4
5
6
7
8
def solution(a, b):
    answer = 0
    c = a**b
    c = str(c)
    answer = c[-1:-6:-1]
    answer = answer[::-1]
    answer = int(answer)
    return answer