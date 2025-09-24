"""
x에서 0을 모두 제거해 -> 1111 그리고 그 다음 len을 이진 변환 함수로 넘겨서 이진으로 변환된 수를 내놔.

4 ->while 현재 != 0일때까지, 나머지를 그 앞에 추가해.
"""

def solution(s):
    answer = [0, 0]
    def to_binary(num):
        result = ""
        while (num != 0):
            result = str(num % 2) + result
            num = num // 2
        return result
    
    while (s != "1"):
        answer[1] += s.count("0")
        s = s.replace("0", "")
        s = to_binary(len(s))
        answer[0] += 1
    
    return answer