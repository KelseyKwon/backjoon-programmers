def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
      stack = []
      for j in range(n):
        c = s[(i+j) % n]
        if c == "(" or c == "[" or c == "{":
          stack.append(c)
        else:
          if not stack:
            break
          if (c == ")" and stack[-1] == "("):
            stack.pop()
          if (c == "]" and stack[-1] == "["):
            stack.pop()
          if (c == "}" and stack[-1] == "{"):
            stack.pop()
      else:
        if not stack:
          answer += 1
    return answer