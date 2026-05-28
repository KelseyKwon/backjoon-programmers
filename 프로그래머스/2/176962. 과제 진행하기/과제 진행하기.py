def solution(plans):
    # 1. 데이터를 처리하기 좋게 가공 (시간을 분 단위 정수로 변환, 정렬)
    converted = []
    for n, s, t in plans:
        h, m = map(int, s.split(':'))
        converted.append([n, h*60+m, int(t)])
    
    # 시작 시간 순으로 과제를 정렬 (시간의 흐름대로 처리하기 위함)
    converted.sort(key=lambda x: x[1])
    
    stack = []      # 잠시 멈춘 과제들을 보관할 스택 (LIFO: 나중에 멈춘 걸 먼저 처리)
    answer = []     # 완료한 과제 이름을 순서대로 담을 리스트
    
    # 2. 과제들을 하나씩 살펴보며 처리
    for i in range(len(converted)):
        name, start, playtime = converted[i]
        
        # 아직 시작하지 않은 다음 과제가 남아있는 경우
        if i < len(converted) - 1:
            next_start = converted[i+1][1] # 다음 과제의 시작 시각
            
            # [경우 1] 현재 과제를 다음 과제 시작 전까지 끝낼 수 있는가?
            if start + playtime <= next_start:
                answer.append(name) # 현재 과제 완료
                
                # 과제를 마치고도 시간이 남았다면? (다음 과제까지의 여유 시간)
                remain = next_start - (start + playtime)
                
                # 스택에 멈춰둔 과제가 있다면 남는 시간에 처리하자
                while stack and remain > 0:
                    s_name, s_time = stack.pop()
                    if s_time <= remain: # 멈췄던 과제도 이번에 완전히 끝낼 수 있다면
                        remain -= s_time
                        answer.append(s_name)
                    else: # 멈췄던 과제를 다 못 끝내면 남은 시간만큼 줄이고 다시 스택에 넣음
                        stack.append([s_name, s_time - remain])
                        remain = 0 # 이제 여유 시간이 없음
            
            # [경우 2] 현재 과제를 다음 과제 시작 전까지 못 끝내는 경우
            else:
                # 현재 과제를 하다가 다음 과제 시작 시간이 되면 중단!
                # 지금까지 한 만큼(next_start - start)을 뺀 나머지 시간을 스택에 저장
                stack.append([name, playtime - (next_start - start)])
        
        # [경우 3] 더 이상 새로 시작할 과제가 없을 때 (마지막 과제)
        else:
            answer.append(name)
    
    # 3. 모든 과제 처리가 끝나고 스택에 남은 과제들을 순서대로 완료 처리
    while stack:
        answer.append(stack.pop()[0])
        
    return answer