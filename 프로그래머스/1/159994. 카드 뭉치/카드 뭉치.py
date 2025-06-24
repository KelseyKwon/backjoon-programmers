from collections import deque

def solution(cards1, cards2, goal):
  answer = 'Yes'
  queue1 = deque()
  queue2 = deque()

  for i in cards1:
    queue1.append(i)
  for i in cards2:
    queue2.append(i)

  for j in goal:
    if (queue1 and queue1[0] == j):
      queue1.popleft()
    elif (queue2 and queue2[0] == j):
      queue2.popleft()
    else:
      answer = 'No'
      break

  return answer