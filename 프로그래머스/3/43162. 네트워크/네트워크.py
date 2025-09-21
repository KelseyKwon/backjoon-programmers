def solution(n, computers):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for nxt, connected in enumerate(computers[v]):  # 인덱스와 값 같이
            if connected == 1 and not visited[nxt]:
                dfs(nxt)

    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt