"""
문자를 stack에 쌓아 -> 그리고 stack이고 ! stack의 top 이 현재랑 같으면 -> pop해. 
"""

def solution(s):
    answer = -1
    
    # b -> a -> a
    # stack = list()
    stack = []
    
    for a in s:
        # if stack and stack.top() == a:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            # stack.push(a)
            stack.append(a)
    
    if stack:
        return 0
    else:
        return 1