def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    w_list = [w.split(',') for w in s_list]

    w_list.sort(key = len)
    for a in w_list:
      for w in a:
        if int(w) not in answer:
          answer.append(int(w))
    return answer