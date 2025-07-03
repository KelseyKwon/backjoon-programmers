from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
  rows = len(maps)
  cols = len(maps[0])

  visited = [[False] * cols for _ in range(rows)]

  def inRange(x, y):
    return 0 <= x < rows and 0 <= y < cols

  def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))

    while q:
      cur_x, cur_y = q.popleft()

      if cur_x == rows-1 and cur_y == cols-1:
        return maps[cur_x][cur_y]
      
      for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if inRange(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
          visited[nx][ny] = True
          q.append((nx, ny))
          maps[nx][ny] += maps[cur_x][cur_y]
    return -1
    
  answer = bfs(0, 0)
  return answer

