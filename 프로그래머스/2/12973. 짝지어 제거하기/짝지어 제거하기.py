def solution(s):
    stack = []

    cur_char = s[0]
    stack.append(cur_char)

    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop(-1)
        else:
            stack.append(s[i])
    
    if (len(stack) == 0):
        return 1
    else:
        return 0
