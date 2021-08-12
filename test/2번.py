# def solution(n, r, c):
#     answer = 0
#
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
# f
#     return answer

# C = sorted(((x, y) for x in range(n) for y in range(n)),
#            key=lambda z:(z[0]+z[1], z[1] if (z[0]+z[1])%2 else z[0]))
# L = [[0] * n for _ in range(n)]
# for i, (x, y) in enumerate(C, 1): L[x][y] = i
# for line in L: print(*line)
# n = 5
# mx = [[0]*n for i in range(n)]
# x, y = 0, 0
# a = 1 # 0=↙, 1=↗
# mx[x][y] = 1
# for i in list(range(2,n**2+1)):
#     if y == 0 and a == 0:
#         if x < n-1: x += 1
#         else: y += 1
#         a = 1
#     elif x == 0 and a == 1:
#         if y < n-1: y += 1
#         else: x += 1
#         a = 0
#     elif y == n-1 and a == 1:
#         x += 1; a = 0
#     elif x == n-1 and a == 0:
#         y += 1; a = 1
#     elif a == 0:
#         x += 1; y += -1
#     elif a == 1:
#         x += -1; y += 1
#     mx[x][y] = i
# print(mx)
# print(mx[0][0])
# print('\n'.join([' '.join(list(map(str,i))) for i in mx]))
n = 5
r = 3
c = 2
def solution(n, r, c):
    start = 1 + ((r+c-2)(r+c-1)/2)
    if r >= n//2:
        if (r+c) % 2 == 0:
            # (r+c-1,1) = start
            result = start + r
        elif (r+c) % 2 == 1:
            # (1,r+c-1) = start
            result = start + c
    else:
        if (r+c) % 2 == 0:
            # (1,r+c-1) = start
            result = start + c
        elif (r+c) % 2 == 1:
            # (r+c-1,1) = start
            result = start + r
    return result

def solution(n, r, c):
    result = 0
    start = 1 + ((r+c-2)(r+c-1)//2)
    if r >= n//2:
        if (r+c) % 2 == 0:
            # (r+c-1,1) = start
            result = start + r
        elif (r+c) % 2 == 1:
            # (1,r+c-1) = start
            result = start + c
    else:
        if (r+c) % 2 == 0:
            # (1,r+c-1) = start
            result = start + c
        elif (r+c) % 2 == 1:
            # (r+c-1,1) = start
            result = start + r
    return result


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
def solution(n, r, c):
    answer = 0
    mx = [[0]*n for i in range(n)]
    x, y = 0, 0
    a = 1
    mx[x][y] = 1
    for i in list(range(2,n**2+1)):
        if y == 0 and a == 0:
            if x < n-1: x += 1
            else: y += 1
            a = 1
        elif x == 0 and a == 1:
            if y < n-1: y += 1
            else: x += 1
            a = 0
        elif y == n-1 and a == 1:
            x += 1; a = 0
        elif x == n-1 and a == 0:
            y += 1; a = 1
        elif a == 0:
            x += 1; y += -1
        elif a == 1:
            x += -1; y += 1
        mx[x][y] = i

    answer = mx[r-1][c-1]

    return answer