def solution(n, wires):
    def dfs(start, visited, graph):
        visited[start] = True
        count = 1
        for k in graph[start]:
            if not visited[k]:
                count += dfs(k, visited, graph)
        return count

    min_diff = float('inf')

    for i in range(len(wires)):
        linked_list = [[]  for _ in range(n+1)]
        for j in range(len(wires)):
            if (i == j):
                continue
            else:
                a, b = wires[j]
                linked_list[a].append(b)
                linked_list[b].append(a)
        visited = [False] * (n+1)
        count = dfs(1, visited, linked_list)

        other = n - count
        min_diff = min(min_diff, abs(count - other))

    return min_diff