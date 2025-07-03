def solution(s):
    answer = 0

    flag_count = 1
    other_count = 0
    flag = s[0]
    for i in range(1, len(s)):
        if flag_count == other_count:
            flag_count = 1
            other_count = 0
            flag = s[i]
            answer +=1
        elif flag == s[i]:
            flag_count += 1
        elif flag != s[i]:
            other_count += 1
            

    return answer+1