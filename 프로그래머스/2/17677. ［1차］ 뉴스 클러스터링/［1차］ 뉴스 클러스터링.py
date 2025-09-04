"""
집합 유사도는 교집합 / 합집합
두 집합이 모두 공집합이면 1로 정의

fr, ra, an, nc, ce / fr, re, en, nc, ch

ha, an, nd, ds, sh, ha, ak, ke / sh, ha, ak, ke, eh, ha, an, nd, ds

1) 영어 아닌거 다 없애.공백도 없애
2) 대문자인거는 다 소문자로 바꿔

"""

from collections import Counter

# def solution(str1, str2):
#     answer = 0
    
#     final_str1, final_str2 = "", ""
#     result1, result2 = [], []
#     for ch in str1:
#         if ch.isalpha():
#             final_str1 += ch.lower()
    
#     for ch in str2:
#         if ch.isalpha():
#             final_str2 += ch.lower()
    
    
#     # 1부터 len(final_str1) - 1까지
#     for i in range(1, len(final_str1)):
#         result1.append(final_str1[:i])
    
#     for i in range(1, len(final_str2)):
#         result2.append(final_str2[:i])
        
#     a = len(list((Counter(a) & Counter(b)).elements()))
#     b = len(list((Counter(a) | Counter(b)).elements()))
        
#     return int(a / b * 65536)

from collections import Counter

def solution(str1, str2):
    def bigrams(s):
        s = s.lower()
        out = []
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if a.isalpha() and b.isalpha():
                out.append(a+b)
        return out
        
    
    a = Counter(bigrams(str1))
    b = Counter(bigrams(str2))
    
    inter = a & b
    union = a | b
    inter_size = sum(inter.values())
    union_size = sum(union.values())
    
    if union_size == 0:
        return 65536
    
    return int(inter_size / union_size * 65536)
