def solution(board):
    answer = 7

    def bfs(arr, visited, s):
        answer = 0
        q = [(s[0], s[1])]
        visited[s[0]][s[1]] = True

        while len(q) != 0:
            x = q.pop(0)
            a = x[0]
            b = x[1]

            visited[a][b] = True
            answer += 1

            if arr[a + 1][b] == 1 and visited[a + 1][b] == False:
                visited[a + 1][b] = True
                q.append((a + 1, b))
            if arr[a - 1][b] == 1 and visited[a - 1][b] == False:
                visited[a - 1][b] = True
                q.append((a - 1, b))
            if arr[a][b + 1] == 1 and visited[a][b + 1] == False:
                visited[a][b + 1] = True
                q.append((a, b + 1))
            if arr[a][b - 1] == 1 and visited[a][b - 1] == False:
                visited[a][b - 1] = True
                q.append((a, b - 1))

        return answer

    n = int(input())
    lines = list(map(str, sys.stdin.readlines()))
    arr = [[0 for i in range(n + 2)] for i in range(n + 2)]
    visited = [[False for i in range(n + 2)] for i in range(n + 2)]
    result = []

    for row, line in enumerate(lines):
        for col, x in enumerate(line):
            if x == '\n':
                break
            arr[row + 1][col + 1] = int(x)

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if arr[x][y] == 1 and visited[x][y] == False:
                result.append(bfs(arr, visited, (x, y)))

    print(len(result))
    for i in sorted(result):
        print(i)

    return answer


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global tx, ty, flag
    if flag: return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M or a[nx][ny] != a[tx][ty]: # 범위 벗어나지 않고, 색깔이 같을 때만 하도록
            continue
        if not visit[nx][ny]:
            visit[nx][ny] = True # 방문처리 했다가
            dfs(nx, ny, cnt + 1)
            visit[nx][ny] = False # 안한 걸로
        else:
            if cnt >= 4 and tx == nx and ty == ny: # 4번 이상이고 위치가 같을 때 -> 사이클
                flag = True
                return

N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
flag = False

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            tx, ty = i, j
            visit[i][j] = True
            dfs(i, j, 1)
        if flag:
            print("Yes")
            exit(0)

print("No")
