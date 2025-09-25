"""
일단 학생별로 맞은 학생을 담는 dictionary 선언
"""

def solution(answers):
    answer = []
    
    scores = {1: 0, 2: 0, 3: 0}
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == answer_1[i % len(answer_1)]:
            scores[1] += 1
        if answers[i] == answer_2[i % len(answer_2)]:
            scores[2] += 1
        if answers[i] == answer_3[i % len(answer_3)]:
            scores[3] += 1
    
    max_score = max(scores.values())
    for k in scores.keys():
        if scores[k] == max_score:
            answer.append(k)
            
    return answer