"""
일단 덩어리를 세야돼.
"""

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur):
        for k in range(n):
            if not visited[k] and computers[cur][k] == 1:
                visited[k] = True
                dfs(k)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1
    return answer