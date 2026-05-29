def solution(s):
    lens = len(s)
    answer = lens
    for i in range(1, lens // 2 + 1):
        count = 1
        prev = s[:i]
        cur_word = ""
        for j in range(i, lens, i):
            cur = s[j:j+i]
            if prev == cur:
                count += 1
                continue
            else:
                _count = "" if count == 1 else str(count)
                cur_word += _count + prev
                prev = cur
                count = 1
            
    # 마지막 처리 
        _count = "" if count == 1 else str(count)
        cur_word += _count + prev
        answer = min(answer, len(cur_word))
        
    return answer
        
        