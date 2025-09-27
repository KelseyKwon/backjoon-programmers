"""

"""

def solution(arr):
    stack = []
    
    for k in arr:
        if stack and stack[-1] == k:
            stack.pop()
            stack.append(k)
        else:
            stack.append(k)
    return stack