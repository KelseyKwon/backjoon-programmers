from collections import deque

def solution(order):
  q = deque([i for i in range(1, len(order) + 1)])
  stack = []
  count = 0

  for i in order:
    if stack and stack[-1] == i:
      count += 1
      stack.pop(-1)
    else:
      while q and q[0] != i:
        stack.append(q.popleft())
      
      if q and q[0] == i:
        count += 1
        q.popleft()
      else:
        break
  return count


