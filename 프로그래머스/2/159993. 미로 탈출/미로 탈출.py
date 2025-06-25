from collections import deque

def bfs(maps, start, target):
  n, m = len(maps), len(maps[0])
  visited = [[False]*m for _ in range(n)]
  queue = deque()
  queue.append((*start, 0))
  visited[start[0]][start[1]] = True

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  while queue:
    x, y, dist = queue.popleft()

    if maps[x][y] == target:
      return dist
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if (0<=nx<n and 0<=ny<m):
        if not visited[nx][ny] and maps[nx][ny] != 'X':
          visited[nx][ny] = True
          queue.append((nx, ny, dist+1))

  return -1

  """
queue에 원소가 있을때까지 : popleft하고, 종료조건이면 리턴하고,
그리고 range(4)동안, nx, ny계산하고, 제약조건을 확인하고, 다 만족하면 visited, queue에 추가하기.
  """



def solution(maps):
    answer = 0
    for row in range(len(maps)):
      for col in range(len(maps[0])):
        if (maps[row][col] == 'S'):
          start= (row, col)
        elif (maps[row][col] == 'L'):
          lever = (row, col)
    
    to_lever = bfs(maps, start, 'L')
    to_exit = bfs(maps, lever, 'E')

    if to_lever == -1 or to_exit == -1:
      return -1

    return to_lever + to_exit