"""
최소거리 -> bfs!

"""
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    q = deque([(0, 0, 1)])
    visited[0][0] = True
    
    def inRange(x, y):
        return 0<=x<rows and 0<=y<cols
    
    while q:
        cur_x, cur_y, cost = q.popleft()
        
        if cur_x == rows - 1 and cur_y == cols - 1:
            return cost
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, cost + 1))
    return -1
