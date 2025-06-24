def solution(N, stages):
  answer = [0 for _ in range(N+2)]

  for i in stages:
    answer[i]+=1
  
  fail_rate = []
  past_num = len(stages)
  for i in range(1, len(answer)-1):
    if answer[i] == 0:
      fail_rate.append(0)
    else:
      fail_rate.append(answer[i] / past_num)
      past_num -= answer[i]
  
  sorted_indices = sorted(range(1, len(fail_rate)+1), key=lambda i : fail_rate[i-1], reverse = True)
  return sorted_indices
