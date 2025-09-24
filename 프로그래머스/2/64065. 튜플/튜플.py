"""
튜플에는 중복 ok, 순서가 다르면 다른 튜플, 원소 개수는 유한하다.
집합은 순서가 바뀌어도 같은 집합.
집합을 길이를 기준으로 정렬해 -> 그리고 
"""

def solution(s):
    answer = []
    temp = set()
    
    s_list = s[2:-2].split("},{")
    w_list = [w.split(",") for w in s_list]
    w_list.sort(key = len)

    for now in w_list:
        for now_num in now:
            cur_num = int(now_num)
            if cur_num not in temp:
                answer.append(cur_num)
                temp.add(cur_num)
                
    
    return answer