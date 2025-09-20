"""
prices의 값은 10000이하 자연수, 길이는 100000이하.

"""

def solution(prices):
    answer = []
    n = len(prices)
    
    # O(N^2)
    for i in range(n):
        cur = prices[i]
        for j in range(i, n):
            if (prices[j] < cur):
                answer.append(j-i)
                break
        else:
            answer.append(n-i-1)
    
    return answer