def solution(number):
    answer = 0
    
    def backtrack(start_idx, count, sums):
        nonlocal answer
        if count == 3:
            if sums == 0:
                answer += 1
            return
        
        for i in range(start_idx, len(number)):
            backtrack(i+1, count + 1, sums + number[i])
    backtrack(0, 0, 0)
    return answer