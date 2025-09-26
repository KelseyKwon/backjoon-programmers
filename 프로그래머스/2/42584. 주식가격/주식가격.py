def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
        
    # 스택에 남아있는 것들은 가격이 떨어지지 않는 것.
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer

"""
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
"""