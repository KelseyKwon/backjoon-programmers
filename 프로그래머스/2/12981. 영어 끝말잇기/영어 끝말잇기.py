import math
def solution(n, words):
    answer = []
    """
    2<= n <= 10
    n<= 배열의 길이 <= 100
    2<= 단어의 길이 <= 50
    [번호, 차례 형태로 return] 하기
    
    1) 이미 존재 하거나 -> set으로 만들고 전과 길이가 같으면 False하거나 ... 
    2) 끝이 맞지 않으면 -> 이전[-1] == 지금[0]이 맞는지.
    
    차례 = (i // n) + 1, 순서 : (i % n) + 1
    """
    word_list = set()
    word_list.add(words[0])
    flag = words[0]
    
    for i in range(1, len(words)):
        if words[i] in word_list or flag[-1] != words[i][0]:
                   return [(i % n) + 1, (i // n) + 1]
                   break
        else: 
            word_list.add(words[i])
            flag = words[i]
    
    return [0, 0]
                   

    return answer