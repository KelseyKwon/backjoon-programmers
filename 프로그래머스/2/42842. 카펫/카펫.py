"""
일단 먼저 b + y = 을 구하고,
더한 거의 반까지 배열을 돌림 : % == 0 이면 i가 세로, 몫이 가로.
여기서 (가로 - 2) * (세로 - 2) == yellow이면,
return 가로, 세로
"""

def solution(brown, yellow):
    answer = []

    total = brown + yellow
    for i in range(2, (total // 2) + 1):
      if (total % i == 0):
        width = total / i
        length = i
        if (width - 2) * (length - 2) == yellow:
          return [width, length]
    