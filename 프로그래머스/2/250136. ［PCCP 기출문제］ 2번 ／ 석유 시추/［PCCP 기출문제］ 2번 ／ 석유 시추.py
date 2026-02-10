"""
0 0 0 1 1 1 0 0
0 0 0 0 1 1 0 0
1 1 0 0 0 1 1 0
1 1 1 0 0 0 0 0
1 1 1 0 0 0 1 1

dfs로 1의 크기를 구해 -> 
-> 상, 하, 좌, 우 탐색해서, 1이면 +1 -> 총 8개!

열의 숫자 위에, 아래 묻힌 총 덩어리의 크기를 저장해

8 8 8 7 7 7 7,2 2

배열에, 탐색한 열을 저장해 -> 그리고, 그 열 만큼 저장하고 끝내
"""
from collections import deque

def solution(land):
    answer = 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N, M = len(land), len(land[0])
    visited = [[0] * M for _ in range(N)]
    
    # 탐색한 열을 저장하기 위해
    gas_land = [[] for _ in range(M)]
    
    def inRange(x, y):
        return 0 <= x < N and 0 <= y < M
    
    def bfs(land, i, j):
        visit_col = set()
        q = deque()
        # q.append((i, j, 0))
        q.append((i, j))
        visit_col.add(j)
        result_amount = 1
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (inRange(nx, ny) and not visited[nx][ny] and land[nx][ny]):
                    result_amount += 1
                    q.append((nx, ny))
                    visit_col.add(ny)
                    visited[nx][ny] = 1
                    
        for col in visit_col:
            gas_land[col].append(result_amount)
        
        
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and land[i][j]:
                visited[i][j] = 1
                bfs(land, i, j)
    answer = max(sum(gas) for gas in gas_land)
    
    return answer