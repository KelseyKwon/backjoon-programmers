count = 0
answer = 0
characters = ['A', 'E', 'I', 'O', 'U']

def dfs(word, next):
    global count, answer
    if word == next:
        answer = count
        return
    
    if len(next) >= 5:
        return
    
    for char in characters:
        count += 1
        dfs(word, next + char)

def solution(word):
    global count, answer
    dfs(word, "")
    return answer