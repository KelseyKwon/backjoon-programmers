def solution(nums):
    answer = 0
    result = set(nums)
    if (len(result) > len(nums) / 2):
      return len(nums) / 2
    else:
      return len(result)