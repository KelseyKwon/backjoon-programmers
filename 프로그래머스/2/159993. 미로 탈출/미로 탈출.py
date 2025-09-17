"""
s -> l가고 l -> e까지

각각 모두 최단거리!!

queue쓰기

다음으로 이동하는 기준 : 범위 안에 있고, x가 아니며, 방문하지 않았으면
"""
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(cur_x, cur_y, target):
        visited = [[False]  * m for _ in range(n)]
        q = deque()
        q.append((cur_x, cur_y, 0))
        visited[cur_x][cur_y] = True
        
        while q:
            x, y, count = q.popleft()
            if (maps[x][y] == target):
                return count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (inRange(nx, ny) and maps[nx][ny] != 'X' and not visited[nx][ny]):
                    q.append((nx, ny, count + 1))
                    visited[nx][ny] = True
                    
        return -1
                    
    
    # maps가 지금 문자열이다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_x , start_y = i, j
            elif maps[i][j] == 'L':
                lever_x, lever_y = i, j
            
    
    to_lever = bfs(start_x, start_y, 'L')
    if to_lever == -1: return -1
    to_exit = bfs(lever_x, lever_y, 'E')
    if to_exit == -1: return -1
    
    return to_lever + to_exit