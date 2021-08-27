"""
[Topics]
dp

[Sketch]
N을 1씩 올려보면서 조합이 어떤 패턴으로 나오는지 본다.

잘 모르겠다
다시 물어보기

"""
def solution(N, number):
    arr = [None] + [{int(str(N)*i)} for i in range(1, 9)]
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in arr[j]:
                for num2 in arr[i-j]:
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2:
                        arr[i].add(num1 // num2)

        if number in arr[i]:
            return i

    return -1
