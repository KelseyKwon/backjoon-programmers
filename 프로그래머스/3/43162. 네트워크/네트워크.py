def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def dfs(cur):
        for k in range(n):
            if computers[cur][k] and not visited[k]:
                visited[k] = True
                dfs(k)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer += 1
    
    return answer