"""
1은 생략 -> 나타난 횟수에 대해서 2a2b이런식으로

for 끊는단위 (1 ~ s/2)
stack으로!
a
"""
import sys

def solution(s):
    n = len(s)
    answer = n # 최악은 그대로의 길이 
    
    def dozip(start, length, s):
        cur_str = []
        prev = start
        count = 1
        for i in range(length, len(s), length):
            temp = s[i:i+length]
            if (prev == temp):
                count += 1
            else:
                # if (count == 1):
                #     cur_str.append(prev)
                # else:
                #     cur_str.append(count + prev)
                cur_str.append((str(count) if count > 1 else "") + prev)
                count = 1
                prev = temp
        cur_str.append((str(count) if count > 1 else "") + prev)
        result_answer = len("".join(cur_str)) #문자로 이루어진 배열을 합치기
        return result_answer
            
    
    for i in range(1, n // 2 + 1): 
        answer = min(answer, dozip(s[:i], i, s))
    
    return answer