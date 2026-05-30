"""
백트래킹!
"""

def solution(word):
    count = 0
    answer = 0
    
    def backtrack(cur_word):
        nonlocal count, answer
        
        if answer > 0:
            return
        
        if cur_word == word:
            answer = count
            return
        
        if len(cur_word) >= 5: 
            return 
        
        for a in ['A', 'E', 'I', 'O', 'U']:
            count += 1
            backtrack(cur_word + a)
    backtrack("")
    return answer
