# 이진 변환 횟구와 제거하는 0의 개수를 answer에 담아 반환하기

# def search(str, answer):
#     if len(str) == 1:
#         return
#     else: 
#         answer[0] += str.count("0")
#         str = str.replace("0", "")
#         answer[1] += 1
#         return search(str, answer)

# def solution(s):
#     answer = [0, 0]
#     search(s, answer)
#     return answer
# def search(str, answer):
#     if str == "1":
#         return answer
#     else: 
#         answer[1] += str.count("0")
#         str = str.replace("0", "")
#         answer[0] += 1
#         str = bin(len(str))[2:]
#         return search(str, answer)

# def solution(s):
#     answer = [0, 0]
#     return search(s, answer)

# def dfs(s, transforms, zeros):
#     if s == "1":
#         return transforms, zeros
    
#     z = s.count("0")
#     zeros += z
#     s = s.replace("0", "")
#     s = bin(len(s))[2:]
#     return dfs(s, transforms+1, zeros)

# def solution(s):
#     t, z = dfs(s, 0, 0)
#     return [t, z]

def solution(s):
    answer = [0, 0]  # [변환 횟수, 제거된 0의 개수]

    while s != '1':
        zero_count = s.count('0')
        s = s.replace('0', '')  # 0 제거
        length = len(s)
        s = bin(length)[2:]  # 길이를 2진수로 변환
        answer[0] += 1
        answer[1] += zero_count

    return answer