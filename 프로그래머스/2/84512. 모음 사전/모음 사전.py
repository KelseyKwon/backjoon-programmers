def solution(word):
    count = 0
    answer = 0
    characters = ['A', 'E', 'I', 'O', 'U']
    def backtrack(cur):
        nonlocal count, answer
        if answer > 0:
            return
        
        if cur == word:
            answer = count
            return
        
        if len(cur) >= 5:
            return
        
        for a in characters:
            count += 1
            backtrack(cur + a)
            
    backtrack("")
    
    return answer