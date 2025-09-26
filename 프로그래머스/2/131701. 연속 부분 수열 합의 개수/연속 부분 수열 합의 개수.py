def solution(elements):
    n = len(elements)
    answer = set()

    for i in range(1, n + 1):  # 길이 1..n
        # 초기 창 합
        temp = sum(elements[:i])
        answer.add(temp)

        # 원형으로 n-1번 밀기 → 총 n개의 창
        for j in range(i, i + n - 1):
            in_value = elements[j % n]               # 새로 들어오는 원소
            out_value = elements[(j - i) % n]        # 창에서 빠지는 원소
            temp += in_value
            temp -= out_value
            answer.add(temp)

    return len(answer)
