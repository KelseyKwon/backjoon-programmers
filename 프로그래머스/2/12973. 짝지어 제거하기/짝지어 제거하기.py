"""
baabaa -> bbaa -> aa -> x


"""

def solution(s):
    answer = -1
    
    s_list = list(s)

    N = len(s)
    prev = s[0]
    for i in range(1, N):
        if prev == s_list[i]:
            s_list.pop(i-1)

    if (len(s_list) == 0):
        return 1
    else:
        return 0