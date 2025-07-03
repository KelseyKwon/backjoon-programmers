from collections import deque

def solution(begin, target, words):
    def bfs(begin, target):
      queue = deque()
      queue.append((begin, 0))

      while queue:
        now, step = queue.popleft()

        if now == target:
          return step

        for i in words:
          count = 0
          for k in range(len(i)):
            if i[k] != now[k]:
              count += 1
          
          if count == 1:
            queue.append((i, step+1))
    
    if target not in words:
      return 0
    return bfs(begin, target)