# answer_count = 0

# def dfs(numbers, result, cur_index, visited, target):
#   if (cur_index == 4):
#     return result

#   for i in range(1, len(numbers)+1):
#     if not visited[i]:
#       visited[i] = True
#       first = dfs(numbers, result+numbers[cur_index], cur_index+1, visited, target)
#       if (first == target):
#         answer_count += 1
#       second = dfs(numbers, result-numbers[cur_index], cur_index+1, visited, target)
#       if (second == target):
#         answer_count += 1



# def solution(numbers, target):
#     visited = [[False] * (len(numbers)+1)]
#     dfs(numbers, 0, 0, visited,)
#     return answer_count

def solution(numbers, target):
  def dfs(index, total):
    if index == len(numbers):
      return 1 if total == target else 0
    
    plus = dfs(index + 1, total + numbers[index])
    minus = dfs(index + 1, total - numbers[index])
    return plus + minus
  return dfs(0, 0)