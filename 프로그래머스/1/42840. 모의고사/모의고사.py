def solution(answers):
    # 수포자들의 찍기 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 각 수포자의 점수
    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for idx, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[idx] += 1

    # 최고 점수 계산
    max_score = max(scores)

    # 최고 점수자만 추출 (1-based index)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result
