import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    queue = deque()

    for i in range(N):
      cur_num = math.ceil((100 - progresses[i]) / speeds[i])
      queue.append(cur_num)
    
    now_num = queue.popleft()
    cnt = 1

    while queue:
      next_num = queue.popleft()
      if (now_num >= next_num):
        cnt += 1
      else:
        answer.append(cnt)
        now_num = next_num
        cnt = 1
    answer.append(cnt)
    return answer