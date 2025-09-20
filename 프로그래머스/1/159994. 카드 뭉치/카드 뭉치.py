"""
순서대로, 한 번만 사용 가능, 순서대로만 사용해야함, 순서 바꾸기 x

Yes or No

각 card 배열의 크기는 1이상 10 이하
서로 다른 단어만 존재.
모두 소문자로만 이루어져 있음.

q1 = deque(cards1), q2 = deque(cards2) 
q1[0] q2[0]중에 매치가 안되면 -> return No

q1[0]이랑 매치 -> q1.popleft()
"""
from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    print("q1: ", q1)
    
    # for word in goal:
    #     if not (word == q1[0] or word == q2[0]):
    #         return "No"
    #     elif (word == q1[0]):
    #         q1.popleft()
    #     elif (word == q2[0]):
    #         q2.popleft()
    for word in goal:
        if q1 and q1[0] == word:
            q1.popleft()
        elif q2 and q2[0] == word:
            q2.popleft()
        else:
            return "No"
    
    return "Yes"