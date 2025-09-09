"""
1 : 갈 수 있는 길
0 : 갈 수 없는 길


bfs -> 상, 하, 좌, 우 확인해서 1이고, 범위 안에 있고, 방문하지 않았으면 -> go
"""
from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * M for _ in range(N)]
    
    def inRange(x, y):
        return 0 <= x < N and 0 <= y < M
    
    def bfs(start_x, start_y):
        if maps[start_x][start_y] == 0:
            return -1
        queue = deque([(start_x, start_y, 1)])   #튜플 하나를 원소로
        visited[start_x][start_y] = True
        
        while queue:
            x, y, cost = queue.popleft()
            if x == N - 1 and y == M - 1:
                return cost
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if inRange(nx, ny) and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cost + 1))  #튜플로 넣기
        return -1

    return bfs(0, 0)
