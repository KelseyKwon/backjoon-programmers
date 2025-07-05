"""
2개를 제거했을때 가장 큰 수 -> 그리디!
1924에서 가장 작은 것을 빼면 됨. k개 만큼
"""

def solution(number, k):
    answer = ''
    stack = []
    
    for s in range(len(number)):
        while stack and k > 0 and stack[-1] < number[s]:
            stack.pop()
            k-=1
        stack.append(number[s])
    return "".join(stack[:len(number)-k])