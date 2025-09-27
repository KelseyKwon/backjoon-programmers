def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for index, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            i = stack.pop()
            answer[i] = index - i
        stack.append(index)
    
    maxx = len(prices) - 1
    while stack:
        cur = stack.pop()
        answer[cur] = maxx - cur
    
    return answer