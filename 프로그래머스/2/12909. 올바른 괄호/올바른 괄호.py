def solution(s):
    answer = True
    
    # 스택으로 풀기
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            if ch == ')':
                stack.pop()
    if stack:
        return False

    return True