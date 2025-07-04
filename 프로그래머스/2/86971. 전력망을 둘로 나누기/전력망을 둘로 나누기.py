import sys

def solution(n, wires):
    def dfs(visited, graph, node):
        visited[node] = True
        count = 1
        for i in graph[node]:
            if not visited[i]:
                count += dfs(visited, graph, i)
        return count
            
    min_diff = sys.maxsize
    # visited = [False] * n
    for i in range(1, (len(wires)+1)):
        visited = [False for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]
        for j in range(1, (len(wires)+1)):
            if ( i == j ):
                continue
            else:
                # wires[j] : [1, 3] 과 같은것.
                graph[wires[j-1][0]].append(wires[j-1][1])
                graph[wires[j-1][1]].append(wires[j-1][0])
        count = dfs(visited, graph, 1)
        other_count = n - count
        min_diff = min(min_diff, abs(count - other_count))
    return min_diff