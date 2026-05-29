from collections import deque

def solution(storage, requests):
    answer = 0
    
    rows, cols = len(storage), len(storage[0])
    grid = [["."] * (cols + 2) for _ in range(rows + 2)]
    
    for i in range(rows):
        for j in range(cols):
            grid[i+1][j+1] = storage[i][j]
            
    def doJige(alpha):
        q = deque([(0, 0)])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = [[False] * (cols + 2) for _ in range(rows + 2)]
        targets = []
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<rows + 2 and 0<=ny<cols + 2 and not visited[nx][ny]:
                    if grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif grid[nx][ny] == alpha:
                        visited[nx][ny] = True
                        targets.append((nx, ny))
        for x, y in targets:
            grid[x][y] = '.'
                        
    
    def doCrane(alpha):
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if grid[i][j] == alpha:
                    grid[i][j] = '.'
    
    for r in requests:
        if len(r) == 1:
            doJige(r)
        else:
            doCrane(r[0])
    
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if grid[i][j] != '.':
                answer += 1
    return answer
            