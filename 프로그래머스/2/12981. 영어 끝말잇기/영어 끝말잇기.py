"""
말한거 또 말하기 x, 규칙 지켜야 함. 
1. 말한거 또 말하기 x : not in set
2. 규칙 지켜야함 : prev저장하고, prev[-1] = cur[0]이면 ok 

1, 2번 중 하나라도 안 지켜지면 return 
순서 : index % n + 1
번호 : index // n + 1 이렇게 반환.

아니면 -> [0, 0] 반환
"""

def solution(n, words):
    answer = []

    prev = words[0]
    said_word = set()
    said_word.add(prev)
    
    for i in range(1, len(words)):
        # 말한거 또 말하기 x
        cur = words[i]
        if cur in said_word or prev[-1] != cur[0]:
            return [i % n + 1, i // n + 1]
        else:
            said_word.add(cur)
            prev = cur
    return [0, 0]