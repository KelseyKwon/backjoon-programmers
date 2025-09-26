"""
만약에 sequence 안에 있으면 -> 인덱스 반환.

아니면 -> 2부터
"""


def solution(sequence, k):
    answer = []
    L, R, total, minCnt = 0, 0, 0, float("inf")
    
    # while R < len(sequence):
    for R in range(len(sequence)):
        total += sequence[R]
        
        while total > k and L <= R:
            total -= sequence[L]
            L += 1
        
        if total == k and minCnt > R - L +1:
            minCnt = R - L + 1
            answer = [L , R]
    
    return answer