from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
#     data = defaultdict(set, {i: [] for i in id_list})
#     count = defaultdict(int, {i: [] for i in id_list})
    
#     for rows in report:
#         a, b = rows.split()
#         data[a].add(b)
    
#     for u, v in data.items():
#         count[v] += 1
    
#     for u, v in count.items():
#         if v < k:
            
    # step1 : 신고자별 신고 대상 저장
    user_reported = defaultdict(set)
    for entry in report:
        reporter, reported = entry.split()
        user_reported[reporter].add(reported)
    
    #step2 : 신고 당한 횟수 세기
    report_count = defaultdict(int)
    for reporter in user_reported:
        for reported in user_reported[reporter]:
            report_count[reported] += 1
    
    #step3 : 정지 대상자 추출
    banned_users = {user for user, count in report_count.items() if count >= k}
    
    #step4 : 메일 수 계산
    for user in id_list:
        cnt = sum(1 for target in user_reported[user] if target in banned_users)
        answer.append(cnt)
    return answer
            
    
    return answer