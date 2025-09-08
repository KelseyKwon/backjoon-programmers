"""
x : 바다, 1~9는 무인도를 나타냄.
상, 하, 좌, 우로 연결되면 하나의 무인도

5 -> 9 -> 1 -> 5 -> 1 -> 3 -> 2 -> 1 -> 1로 가 근데 이미 방문 (안방문)

dfs!

모든 배열의 값에 대해서, X가 아니고, 숫자이면, dfs수행
dfs내부에서는:
if 숫자이고, x가 아니면 -> 계속 글로 가면서 해당 값의 숫자를 더해.
그리고 visited 처리해
"""

from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    grid = [list(row) for row in maps]           # 문자 격자
    visited = [[False] * M for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = []
    
    def inRange(x, y):
        return 0 <= x < N and 0 <= y < M
    
    def bfs(sx, sy):
        visited[sx][sy] = True
        q = deque([(sx, sy)])
        days = int(grid[sx][sy])
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if inRange(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 'X':
                    visited[nx][ny] = True
                    days += int(grid[nx][ny])
                    q.append((nx, ny))
        return days
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] != 'X':
                answer.append(bfs(i, j))
    
    return sorted(answer) if answer else [-1]