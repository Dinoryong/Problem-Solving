"""
[Topics]
구현
deep copy

[Sketch]
board 크기가 4 * 4 고정이니까 완탐 가능
or
bfs
백트래킹

"""
from collections import deque
import copy

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def end_game(b):
    if b.count("0") == 16:
        return True
    return False

def remove_element(b, e):
    b = b.replace(e, "0")
    return b

def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if ny >= 0 and ny < 4 and nx >= 0 and nx < 4 and b[ny * 4 + nx] == "0":
        return move(b, ny, nx, dy, dx)
    else:
        if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
            return (ny, nx)
        else:
            return (y, x)

def solution(board, r, c):
    answer = 0
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])
    q = deque([])

    cnt = 0
    enter = -1 # enter을 클릭했던 위치
    q.append((r, c, b, cnt, enter))
    s = set()

    while q:
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s:
            continue
        s.add((y, x, b, e))

        if end_game(b):
            return c

        # 4 방향 이동
        for (dy, dx) in d:
            ny, nx = y + dy, x + dx
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, c+1, e))

        # Ctrl + 4 방향 이동
        for (dy, dx) in d:
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c+1, e))

        # enter를 하는 경우
        if b[pos] != 0:
            if e == -1:
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else:
                if e != pos and b[e] == b[pos]:
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer

# https://bladejun.tistory.com/130
import sys, copy

from itertools import permutations
from collections import deque


def ctrl_move(x, y, d):
    global board_c
    while True:
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            return x, y

        else:
            if board_c[nx][ny] != 0:
                return nx, ny
            x, y = nx, ny


def bfs(sx, sy, ex, ey):
    global board_c

    dic = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

    if sx == ex and sy == ey:
        return 1

    q = deque([[sx, sy]])
    table = [[0] * 4 for _ in range(4)]
    visited = [[True] * 4 for _ in range(4)]
    visited[sx][sy] = False

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1  # enter를 누르기때문에 +1
                q.append([nx, ny])

            nx, ny = ctrl_move(x, y, dic[i])
            if visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1  # enter를 누르기때문에 +1
                q.append([nx, ny])


def remove_card(card):
    global board_c, card_position
    for x, y in card_position[card]:
        board_c[x][y] = 0


def restore_card(card):
    global board_c, card_position
    for x, y in card_position[card]:
        board_c[x][y] = card


def go(sx, sy, order, card_num, count, move):
    global answer, order_p, card_position, board_c
    if count == card_num:
        answer = min(answer, move)
        return

    card = order_p[order][count]

    left = card_position[card][0]
    right = card_position[card][1]

    d1 = bfs(sx, sy, left[0], left[1])  # 출발 지점 -> 해당카드 왼쪽
    d2 = bfs(left[0], left[1], right[0], right[1])  # 해당카드 왼쪽 -> 해당카드 오른쪽

    remove_card(card)
    go(right[0], right[1], order, card_num, count + 1, move + d1 + d2)
    restore_card(card)

    d1 = bfs(sx, sy, right[0], right[1])  # 출발 지점 -> 해당카드 오른쪽
    d2 = bfs(right[0], right[1], left[0], left[1])  # 해당카드 오른쪽 -> 해당카드 왼쪽

    remove_card(card)
    go(left[0], left[1], order, card_num, count + 1, move + d1 + d2)
    restore_card(card)


def solution(board, r, c):
    global answer, order_p, card_position, board_c

    answer = sys.maxsize
    board_c = copy.deepcopy(board)
    card_position = {}

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0:
                if num in card_position.keys():
                    card_position[num].append([i, j])
                else:
                    card_position[num] = [[i, j]]

    orders = [k for k, v in card_position.items()]
    order_p = list(permutations(orders, len(orders)))  # 제거 순서

    for i in range(len(order_p)):
        go(r, c, i, len(card_position.keys()), 0, 0)

    return answer