"""

"""

def solution(numbers, target):
    def dfs(cur, index):
        if (index == len(numbers)):
            return 1 if cur == target else 0
        plus = dfs(cur + numbers[index], index+1)
        minus = dfs(cur - numbers[index], index+1)
        return plus + minus
    return dfs(0, 0)