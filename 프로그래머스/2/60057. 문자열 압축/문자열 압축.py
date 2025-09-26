# 단어 앞에서부터 -> 1부터 2/len(s) + 1까지
# stack에 쌓아. 그리고 stack[-1]이랑 같을때까지 반복해
# 
import sys

def solution(s):
    answer = sys.maxsize
    
    if (len(s)) == 1:
        return 1
    
    
    for i in range(1, len(s) // 2 + 1):
        prev = s[:i]
        count = 1
        candidate = []
        for step in range(i, len(s), i):
            cur = s[step:step+i]
            if cur == prev:
                count += 1
            else:
                if count > 1:
                    candidate.append(str(count))
                candidate.append(prev)
                prev = cur
                count = 1
        if count > 1:
            candidate.append(str(count))
        candidate.append(prev)
            
        cur_answer = "".join(candidate)
        answer = min(answer, len(cur_answer))
        
    return answer