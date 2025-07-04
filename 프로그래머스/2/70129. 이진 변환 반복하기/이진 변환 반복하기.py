"""
이진 변환 과정:
1. 0 없애 -> 0count를 result[1]에 더해
2. 길이 구해
3. 길이를 이진으로 변환해

모든 단계 마다 result[0] += 1

그리고 1이면 나와

"""

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += s.count('0')
        s = s.replace('0', '')
        len_s = len(s)
        s = bin(len_s)[2:]
        answer[0] += 1
    
    return answer