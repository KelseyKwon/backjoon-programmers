"""
회전 -> 나머지로
stack & stack[-1] == 현재
"""

def solution(s):
    answer = 0
    
    n = len(s)
     # 0 1 2 3 4 5 -> 1 2 3 4 5 0 
    
    for i in range(n):
        stack = []
        for j in range(i, i+n):
            cur = j % n
            if stack:
                if stack[-1] == "[" and s[cur] == "]":
                    stack.pop()
                elif stack[-1] == "(" and s[cur] == ")":
                    stack.pop()
                elif stack[-1] == "{" and s[cur] == "}":
                    stack.pop()
                else:
                    stack.append(s[cur])
            else:
                stack.append(s[cur])
        if not stack:
            answer += 1

    return answer