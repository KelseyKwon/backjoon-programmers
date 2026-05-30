"""
삼총사를 만들기! 
순서는 상관 없음.

"""

def solution(number):
    result = 0
    n = len(number)
    
    for i in range(n):
        for j in range(i+1, n):
            flag = number[i] + number[j]
            cur = number[j+1:].count(-flag)
            result += cur
    
    return result