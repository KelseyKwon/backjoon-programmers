# import math

# def solution(n, stations, w):
#     answer = 0
#     def inRange(index):
#       return index >= 1 and index <= n

#     # 전파가 전달되는 기지국
#     visited = [False] * n
#     for i in stations:
#       for j in range(i-w, i+w+1):
#         if inRange(j):
#           visited[j-1] = True
    
#     count = 0
#     for i in range(len(visited)):
#       if (visited[i]):
#         answer += math.ceil(count / (2*w+1))
#         count = 0
#       else:
#         count += 1
#         print(i, count)
#     answer += math.ceil(count / (2*w + 1))

#     return answer

import math

def solution(n, stations, w):
    answer = 0
    ranges = 2*w + 1
    
    cur = 1
    for i in stations:
      if i - w > cur:
        gap = (i-w) - cur
        answer += math.ceil(gap / ranges)
      cur = i + w + 1
    # 남은 구간
    if cur <= n:
      gap = n - cur + 1
      answer += math.ceil(gap / ranges)
    return answer