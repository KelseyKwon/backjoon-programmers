"""
상, 하, 좌, 우 중에 벽까지~ 아니면 D까지~
최소! -> bfs! -> queue!
"""
from collections import deque

def solution(board):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                initial_x, initial_y = i, j
    
    q = deque([(initial_x, initial_y, 0)])
    visited = [[False] * m for _ in range(n)]
    
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    while q:
        cur_x, cur_y, cnt = q.popleft()
        
        if (board[cur_x][cur_y] == 'G'):
            return cnt
        
        for i in range(4):
            nx, ny = cur_x, cur_y
            while inRange(nx+dx[i], ny+dy[i]) and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
            
    return -1