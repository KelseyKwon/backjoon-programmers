def solution(n, words):
    set_words = set()
    set_words.add(words[0])

    for i in range(1, len(words)):
        # 이전 단어의 끝과 현재 단어의 첫 글자 비교 + 중복 확인
        if words[i - 1][-1] != words[i][0] or words[i] in set_words:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        set_words.add(words[i])

    return [0, 0]

"""
def solution(n, words):
    N = len(words)
    a, b = 0, 0
    set_words = set()
    set_words.add(words[0])

    for i in range(1, N):
      if (words[i-1][-1] != words[i][0]) or (len(set_words) == len(set_words.add(words[i]))):
        if (i % N == 0): a = N
        else: a = i%N
        b = (i-1)/n+1
        break
      else:
        set_words.add(words[i])


    return [a, b]
"""