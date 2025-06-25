def valid_point(x, y):
  return (0<=x<=10 and 0<=y<=10)

def move_point(x, y, dir):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  if dir == 'U':
    return x + dx[0],  y + dy[0]
  elif dir == 'R':
    return x + dx[1],  y + dy[1]
  elif dir == 'D':
    return x + dx[2],  y + dy[2]
  else:
    return x + dx[3],  y + dy[3]


def solution(dirs):
    answer = set()
    x, y = 5, 5
    for dir in dirs:
      nx, ny = move_point(x, y, dir)
      if (valid_point(nx, ny)):
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny
    return len(answer)//2