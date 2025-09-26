def solution(skill, skill_trees):
    answer = 0
    
    for k in skill_trees:
        filtered = "".join([c for c in k if c in skill])
        if skill.startswith(filtered):
            answer += 1
    
    return answer