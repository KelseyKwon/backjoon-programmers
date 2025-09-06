"""
1) 이전에 등장했던 단어 / 2) 한 글자인 단어
들은 인정되지 않음

사람수는 10명 이하
단어의 길이는 2이상 50 이하
번호, 차례 형태로 return하기 / 탈락자가 안 생기면 [0, 0]을 return하기

task1 : 이미 등장했던 단어는? -> dict으로 처리
task2 : 앞의 끝 문자로 끝나는지는? -> 일단 앞의 단어를 저장하고 -> 그 다음에 [-1] = [0]인지 확인
task3 : result는 어떻게 반환해? -> 현재 index를 
0, 1, 2 -> [1, 1] [2, 1] [3, 1]
3, 4, 5 -> [1, 2] [2, 2] [3, 2]
6, 7, 8 -> [1, 3] [2, 3] [3, 3] index % 3 + 1 / ceil(index + 1 / 3)

"""
from collections import defaultdict
import math

def solution(n, words):
    m = len(words)
    count = defaultdict(int)
    prev_word = words[0]
    count[prev_word] += 1
    
    for i in range(1, m):
        # 이미 등장했는지 확인
        if (count[words[i]] != 0):
            return [i % n + 1, math.ceil((i + 1) / n)]
        
        # 앞의 단어의 끝과 안 맞는지 확인
        if (prev_word[-1] != words[i][0]):
            return [i % n + 1, math.ceil((i + 1) / n)]
        
        prev_word = words[i]
        count[prev_word] += 1

    return [0, 0]