"""
리스트 시간 초과나 
-> 근데 개수 세는 건 아니야
"""

def solution(numbers):
    stack = []
    n = len(numbers)
    result = [-1 for _ in range(n)]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            num = stack.pop()
            result[num] = numbers[i]
        stack.append(i)
    
    return result
    