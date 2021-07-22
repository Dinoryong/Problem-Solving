# sol 1. dfs bfs
def solution(places):
    answer = []

    size = 5

    def valid(r, c):
        return -1 < r < size and -1 < c < size

    def check(x, y, place):
        dist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and place[nx][ny] == 'P':
                return False

        dist = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and place[nx][ny] == 'P' and (place[x][ny] != 'X' or place[nx][y] != 'X'):
                return False

        dist = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        for dx, dy in dist:
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and place[nx][ny] == 'P' and place[x + dx // 2][y + dy // 2] != 'X':
                return False
        return True

    for place in places:
        flag = False
        for r, c in [(i, j) for i in range(5) for j in range(5)]:
            if place[r][c] == 'P':
                result = check(r, c, place)
                if not result:
                    answer.append(0)
                    flag = True
                    break
        if not flag:
            answer.append(1)

    return answer

#
def solution(places):
    answer = []
    for p in places:
        answer.append(check(p))
    return answer

def check(p):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(5):
        for y in range(5):
            if p[x][y] == "P":
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                        continue
                    if p[nx][ny] == "X":
                        continue
                    if p[nx][ny] == "P":
                        return 0
                    for i in range(4):
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if nnx == x and nny == y:
                            continue
                        if nnx < 0 or nny < 0 or nnx >= 5 or nny >= 5:
                            continue
                        if p[nnx][nny] == "X":
                            continue
                        if p[nnx][nny] == "P":
                            return 0

    return 1

# sol 2. 이중 for 문 (이 문제에서는 대기실 크기가 크지 않고 고정이므로)
def solution(places):
    answer = []

    # place를 하나씩 확인
    for p in places:

        # 거리두기가 지켜지지 않음을 확인하면 바로 반복을 멈추기 위한 key
        key = False
        nowArr = []

        # 이번 place를 nowArr에 담아줍니다.
        for n in p:
            nowArr.append(list(n))

        # 이중 for문을 이용해 하나씩 확인합니다.
        for i in range(5):
            if key:
                break

            for j in range(5):
                if key:
                    break

                # 사람을 찾아내면 판단을 시작합니다.
                if nowArr[i][j] == "P":

                    if i + 1 < 5:
                        # 만약 바로 아랫부분에 사람이 존재하면 break
                        if nowArr[i + 1][j] == "P":
                            key = True
                            break
                        # 만약 아랫부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i + 1][j] == "O":
                            if i + 2 < 5:
                                if nowArr[i + 2][j] == "P":
                                    key = True
                                    break
                    # 바로 오른쪽 부분에 사람이 존재하면 break
                    if j + 1 < 5:
                        if nowArr[i][j + 1] == "P":
                            key = True
                            break
                        # 만약 오른쪽 부분이 빈테이블이고 그 다음에 바로 사람이 있다면 한칸 떨어져 있더라도 맨허튼 거리는 2이므로 break
                        if nowArr[i][j + 1] == "O":
                            if j + 2 < 5:
                                if nowArr[i][j + 2] == "P":
                                    key = True
                                    break
                    # 우측 아래 부분입니다.
                    if i + 1 < 5 and j + 1 < 5:
                        # 만약 우측 아래가 사람이고, 오른 쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j + 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j + 1] == "O"):
                            key = True
                            break

                    # 좌측 아래부분입니다.
                    if i + 1 < 5 and j - 1 >= 0:
                        # 만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j - 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j - 1] == "O"):
                            key = True
                            break

        # 위의 for문동안 key가 True로 변경되었다면 거리두가기 지켜지지 않은것 이므로 0을 answer에 추가
        if key:
            answer.append(0)
        else:
            # key가 false로 끝났다면 거리두기가 지켜졌으므로 1 추가
            answer.append(1)

    # 끝!
    return answer
