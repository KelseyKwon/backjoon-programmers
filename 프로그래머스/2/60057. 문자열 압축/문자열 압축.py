"""
s의 반까지만 하기
그리고 최소 길이를 갱신
1부터 s의 반까지
"""

def solution(s):
    if (len(s) == 1): return 1
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        prev = s[:i]
        _ans = ""
        count = 1
        
        for j in range(i, len(s), i):
            cur = s[j:j+i]
            if prev == cur:
                count += 1
            else:
                # if count != 1:
                #     _ans += cur
                # else:
                #     _ans += str(count) + cur
                _ans += (str(count) if count > 1 else "") + prev
                prev = cur
                count = 1
        _ans += (str(count) if count > 1 else "") + prev
        answer = min(answer, len(_ans))
    return answer