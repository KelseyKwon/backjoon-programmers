"""
최단 거리 -> bfs!!

0이 갈 수 없는거, 1이 갈 수 있는거. 
queue에 거리를 담아.


"""
from collections import deque

def solution(maps):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n = len(maps)
    m = len(maps[0])
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x, y):
        visited = [[False]*m for _ in range(n)] 
        q = deque([(x, y, 1)])
        visited[x][y] = True
        while q:
            cur_x, cur_y, cost = q.popleft()
            
            if (cur_x == n-1 and cur_y == m-1):
                return cost
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                
                if (inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 0):
                    q.append((nx, ny, cost + 1))
                    visited[nx][ny] = True  
        return -1
        
    return bfs(0, 0)