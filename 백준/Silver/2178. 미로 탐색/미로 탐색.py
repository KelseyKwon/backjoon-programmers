from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def inRange(x, y):
  return x >= 0 and x < n and y >= 0 and y < m

def bfs():
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = True

  #각 칸 까지의 거리 저장
  dist = [[0] * m for _ in range(n)]
  dist[0][0] = 1

  while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
      return dist[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (inRange(nx, ny) and not visited[nx][ny] and grid[nx][ny]):
        queue.append((nx, ny))
        visited[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1
  return -1

    

n, m = map(int, input().split())
visited = [[False] * m for _ in range (n)]
grid = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())