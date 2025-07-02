from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(p, idx) for idx, p in enumerate(priorities)])

    while q:
      cur = q.popleft()
      if any(cur[0] < nxt[0] for nxt in q):
        q.append(cur)
      else:
        answer += 1
        if cur[1] == location:
          return answer


