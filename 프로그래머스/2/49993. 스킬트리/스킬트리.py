"""
skill : 선행 스킬 순서
skill_trees : 유저들이 만든 스킬트리

가능한 skill_trees들의 개수를 모두 구하기!
1<= skill <= 26
1<= skill_trees <= 20

1 <= skill_trees 원소 <= 26

skill_trees의 각 원소마다 : 만약에 해당 문자가 skill에 있다면:
처음부터 지금까지 쪼개고 ; (BA) BA에 C 이전의 값 이 존재하면 false.
"""

# def solution(skill, skill_trees):
#     answer = 0
#     skill_list = list(skill)

#     for sk in skill_trees:
#         isValid = True
#         for index, char in enumerate(sk):
#             if char in skill_list:
#                 pre_skill_trees_list = list(sk[:index])
#                 where = skill.find(char)
#                 pre_skill_list = list(skill[:where])

#                 for k in pre_skill_trees_list:
#                     if k not in pre_skill_list: isValid = False; break

#         if (isValid): answer += 1

#     return answer

def solution(skill, skill_trees):
    answer = 0

    for sk in skill_trees:
        learned = [c for c in sk if c in skill]      # 1) 스킬트리 중 선행 스킬만 뽑는다
        learned_str = "".join(learned)

        # 2) 뽑아낸 순서(learned_str)가 skill의 접두사(prefix)인지 확인
        if skill.startswith(learned_str):
            answer += 1

    return answer