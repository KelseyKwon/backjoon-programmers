"""
    최단거리 -> bfs -> queue -> 2차원이니까 dx, dy 정의 , 배열에 count 더하기
    """
from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x, y):
        q = deque()
        q.append((x, y, 1))
        visited[x][y] = True
        
        while q:
            cur_x, cur_y, dist = q.popleft()
            if cur_x == n-1 and cur_y == m-1:
                return dist
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                
                if inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))
                    
        return -1
                    
        
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    return bfs(0, 0)
    