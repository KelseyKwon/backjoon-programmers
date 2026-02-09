"""
상대팁 진영에 도착하기 위해서 지나야 하는 칸의 최솟값

도착 x -> -1 return!

1이면 o, 

상하좌우 살펴보고 -> 0이면 x, 

0, 0 -> n, m으로 가야함. 

bfs!
"""
from collections import deque

def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])
    # visited = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    def inRange(x, y):
        return (x >= 0 and x < N and y >= 0 and y < M)
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque([(0, 0, 1)])
    
    while q:
        cur_x, cur_y, dis = q.popleft();
        if (cur_x == N - 1 and cur_y == M - 1):
            return dis
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if (inRange(nx, ny) and maps[nx][ny] and not visited[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))
    
    return answer