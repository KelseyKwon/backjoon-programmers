"""
queue 선언.

각 지점에서, 'X'가 아니면 -> dfs(x, y)
queue.append해 -> 그다음에 range(4)동안 nx해 -> 
inRange() & not visited & maps != 'X':
.append(x, y, answer)
"""
from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    def dfs(x, y, food):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        total = int(maps[x][y])
        
        while q:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                
                if (inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X'):
                    total += int(maps[nx][ny])
                    visited[nx][ny] = True
                    q.append((nx, ny))
        return total
        
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(dfs(i, j, int(maps[i][j])))
    
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer