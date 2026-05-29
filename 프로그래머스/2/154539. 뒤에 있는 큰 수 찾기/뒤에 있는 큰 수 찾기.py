"""
차례대로 살펴보면 시간 초과 나.

-> stack? 백트래킹?
stack으로 가자. (while)
"""
def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        cur_num = numbers[i]
        if stack:
            while stack and numbers[stack[-1]] < cur_num:
                result[stack[-1]] = cur_num
                stack.pop()
        stack.append(i) # [3, 3, 5]
    
    return result