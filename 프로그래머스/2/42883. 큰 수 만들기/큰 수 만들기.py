"""
stack을 이용해보자!

[1, 9, 2, 4]

"""

def solution(number, k):
    stack = []
    
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        
        stack.append(number[i])
    
    return "".join(stack[:len(number) - k])