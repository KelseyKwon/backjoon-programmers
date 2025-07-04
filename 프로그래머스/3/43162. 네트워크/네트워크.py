def solution(n, computers):
    answer = 0
    
    def dfs(node):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                dfs(i)
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if (i == j): 
                continue
            elif(computers[i][j] == 1):
                graph[i].append(j)
    for k in range(n):
        if not visited[k]:
            dfs(k)
            answer += 1
                
    return answer