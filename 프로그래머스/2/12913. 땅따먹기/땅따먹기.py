def solution(land):
  rows = len(land)
  cols = len(land[0])

  dp = [[0] * cols for _ in range(rows)]
  dp[0] = land[0].copy()

  for row in range(1, rows):
    for col in range(cols):
      best_prev = max(dp[row-1][k] for k in range(cols) if k != col)
      dp[row][col] = land[row][col] + best_prev
  return max(dp[-1])



