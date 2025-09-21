"""
이전에 등장했던 단어 x & 한 글자인 단어는 인정되지 x


"""

def solution(n, words):
    spoken_word = {words[0]}
    m = len(words)
    
    for i in range(1, len(words)):
        prev = words[i-1]
        cur = words[i]
        # 규칙 위반: 끝 글자 불일치 or 중복 단어
        if prev[-1] != cur[0] or cur in spoken_word:
            return [i % n + 1, i // n + 1]
        spoken_word.add(cur)               # 검증 통과 후에 추가
    return [0, 0]