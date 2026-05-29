"""
R -> G
D을 만나면 안됨.

7번을 움직여야 함!
"""
from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    barriers = []
    
    for i in range(rows):
        for j in range(cols):
            if (board[i][j] == 'R'):
                start_x, start_y = i, j
                
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y, count= q.popleft()
        
        if board[x][y] == 'G':
            return count
        
        for i in range(4):
            nx, ny = x, y
            while 0<=nx+dx[i]<rows and 0<=ny+dy[i]<cols and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, count+1))
                
    return -1
    