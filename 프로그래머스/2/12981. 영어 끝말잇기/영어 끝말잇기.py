"""
이전에 말한 단어 사용 x
한글자인 단어 인정 x
마지막 사람 -> 1번부터 다시 시작...

0, 1, 2, 3, 4, 5

index % n -> 0, 1, 2

set에 추가하고, 
1. 그 직전 배열의 길이랑 같거나
2. 끝에가 다르거나,

-> return
0 // 3 -> 0
번호 : i % n + 1, i // n + 1

"""

def solution(n, words):
    answer = [0, 0]
    
    prev_word = words[0]
    no_duplicate_word = set([words[0]])
    for i in range(1, len(words)):
        cur_num = i % n + 1
        cur_turn = i // n + 1
        
        # 중복되면 리턴
        if words[i] in no_duplicate_word:
                return [cur_num, cur_turn]
        if (prev_word[-1] != words[i][0]):
                return [cur_num, cur_turn]
            
        no_duplicate_word.add(words[i])
        prev_word = words[i]
    
    return answer