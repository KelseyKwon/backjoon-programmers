"""
참여 선수, 완주 선수 -> participant, completion

set을 이용해서??? 


"""
# from collections import Counter
# def solution(participant, completion):
#     answer = ''
    
#     partici_set = set(participant)
#     comple_set = set(completion)
    
#     pre_answer = partici_set - comple_set
#     if (not pre_answer):
#         # 2명인 사람 반환
#         cnt = Counter(participant)
#         return [k for k, v in cnt.items() if v == 2]
#     else:
#         return pre_answer[0]
#     return answer

from collections import Counter
def solution(participant, completion):
    cnt = Counter(participant) - Counter(completion)
    return next(iter(cnt));
