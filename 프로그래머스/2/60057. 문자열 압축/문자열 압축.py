import sys
input = sys.stdin.readline

def compress(s, size):
    # size 단위로 자른 뒤 압축 결과 문자열 반환
    chunks = [s[i:i+size] for i in range(0, len(s), size)]
    prev = chunks[0]
    count = 1
    result = []

    for cur in chunks[1:]:
        if cur == prev:
            count += 1
        else:
            # 그룹 끝났을 때
            if count > 1:
                result.append(str(count))
            result.append(prev)
            prev = cur
            count = 1

    # 마지막 그룹
    if count > 1:
        result.append(str(count))
    result.append(prev)

    return ''.join(result)

def solution(s):
    # s 길이가 1이면 바로 1
    if len(s) == 1:
        return 1

    best = len(s)  # 아무 압축도 안 했을 때 원본 길이
    # 1 ~ len(s)//2 까지 모든 단위 시도
    for size in range(1, len(s)//2 + 1):
        compressed = compress(s, size)
        best = min(best, len(compressed))

    return best



