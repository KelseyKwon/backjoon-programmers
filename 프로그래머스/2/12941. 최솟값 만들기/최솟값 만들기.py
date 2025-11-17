"""
가장 작은 숫자 -> 가장 큰 숫자랑 곱해
[1, 2, 4] [5, 4, 4] 
[1, 2] [4, 3] -> 4 + 6


"""

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)
    
    for a, b in zip(A, B):
        answer += a*b
    

    return answer