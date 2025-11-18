"""
1, 2, 3번 서로 돌아가며 -> modulo 연산!
앞사람이 안말한거 / 이전에 안등장한거 / 한글자가 아닌거

안말한거? -> set ! in set인지
한글자가 아닌거? -> length

번호
0 -> 1 i % n + 1
1 -> 2
2 -> 3
3 -> 1

8 -> 3 

차례
0 // 3 + 1
3 // 3 + 1
4 // 3 + 1
5 // 3 + 1
"""

def solution(n, words):
    answer = []

    m = len(words)
    prev = words[0]
    said_word = set()
    said_word.add(prev)
    
    for i in range(1, m):
        cur = words[i]
        person, turn = (i % n) + 1 , (i // n) + 1
        
        if cur in said_word:
            print(person, turn)
            return [person, turn]
        
        if prev[-1] != cur[0]:
            return [person, turn]
        
        said_word.add(cur)
        prev = cur
        
    
    return [0, 0]