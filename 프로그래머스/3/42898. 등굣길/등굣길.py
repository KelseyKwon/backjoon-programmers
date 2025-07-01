# def solution(m, n, puddles):
#     answer = 0
#     dp = [[0] * (m+1) for _ in range(n+1)]
#     for i in range(1, n+1):
#       for j in range(1, m+1):
#         if (i == 1) or (j == 1):
#           dp[i][j] = 1
#         else:
#           dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     answer = dp[n][m]
#     for col, row in puddles:
#       extract = dp[row][col] * dp[n-row][m-col]
#       answer -= extract
#     return answer

def solution(m, n, puddles):
  MOD = 1_000_000_007
  # puddles_set = set((row, col) for col, row in puddles)
  puddles_set = {(row, col) for col, row in puddles}

  dp = [[0] * (m+1) for _ in range(n+1)]

  dp[1][1] = 1

  for i in range(1, n+1):
    for j in range(1, m+1):
      if j == 1 and i == 1:
        continue
      if (i, j) in puddles_set:
        dp[i][j] = 0
      else:
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
  
  return dp[n][m]
      