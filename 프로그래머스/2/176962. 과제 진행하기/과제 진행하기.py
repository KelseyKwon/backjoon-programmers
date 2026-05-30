def solution(plans):
    converted_plans = []
    
    for p in plans:
        sub, start, remained = p
        h, m = map(int, start.split(":"))
        converted_plans.append((sub, h * 60 + m, int(remained)))
    
    converted_plans.sort(key = lambda x:x[1])
    stack = []
    answer = []
    
    for i in range(len(converted_plans)):
        sub, start, remained = converted_plans[i]
        
        # 새로 시작하는 과제 존재
        if i < len(converted_plans) - 1:
            _next = converted_plans[i+1][1]
            remain = _next - start - remained
            
            if remain >= 0:
                answer.append(sub)
                while stack and remain > 0:
                    _name, _time = stack.pop()
                    if _time <= remain:
                        remain -= _time
                        answer.append(_name)
                    else:
                        stack.append((_name, _time - remain))
                        remain = 0
            else:
                stack.append((sub, remained - (_next - start)))
                
        else:
            answer.append(sub)
    
    while stack:
        answer.append(stack.pop()[0])
    return answer
            