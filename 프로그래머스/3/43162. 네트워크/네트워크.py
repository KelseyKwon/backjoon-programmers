def solution(n, computers):
  count = 0
  visited = [False] * n

  def dfs(node):
    visited[node] = True

    for i in range(n):
      if not visited[i] and computers[node][i]:
        dfs(i)

  for i in range(n):
    if not visited[i]:
      dfs(i)
      count += 1

  return count