"""
[프로그래머스 : K번째수]
sol link :

[topics]
Array

[sketch]

"""
# 틀린 이유 : 변수에 command[x] 를 할당해줘야한다
# sort 할 때는 array.sort() 를 바로 해주면 된다.
def solution(array, commands):
    answer = []
    for command in commands:
        command[0] = i
        command[1] = j
        command[2] = k
        arr = array[i-1:j]
        arr = arr.sort()
        answer.append(arr[k-1])
    return answer

#
def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer







