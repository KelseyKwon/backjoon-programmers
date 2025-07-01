alphabet = ['A', 'E', 'I', 'O', 'U']
count = 0
answer = 0

def dfs(word, current):
    global count, answer
    if current == word:
        answer = count
        return
    if len(current) >= 5:
        return

    for char in alphabet:
        count += 1
        dfs(word, current + char)

def solution(word):
    global count, answer
    count = 0
    answer = 0
    dfs(word, "")
    return answer