"""
1. 일단 maps를 1 -> 2차원 배열로
2. bfs : 상, 하, 좌, 우를 탐색하고 -> queue.append(해당 칸의 좌표, 먹이량) 더해.
3. 그리고 다 했으면 -> answer.append()
"""
from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    
    # #maps[0]의 length만큼, 각 maps
    # map = [[maps[i][j] for j in range(m)] for i in range(n)]
    # print(map)
    visited = [[False] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def inRange(x, y):
        return 0<=x<n and 0<=y<m
    
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        total = int(maps[x][y])
        
        while q:
            cur_x, cur_y= q.popleft()
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]
                
                if inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    total += int(maps[nx][ny])
        return total
            
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
    
    # if (len(answer) == 0):
    if not answer:
        # answer.append[-1]
        return [-1]
    answer.sort()
    return answer