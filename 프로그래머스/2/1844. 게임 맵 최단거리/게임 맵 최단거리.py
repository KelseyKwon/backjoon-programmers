from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def inRange(x, y):
        return 0 <= x < n and 0 <= y < m

    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    distance[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return -1

