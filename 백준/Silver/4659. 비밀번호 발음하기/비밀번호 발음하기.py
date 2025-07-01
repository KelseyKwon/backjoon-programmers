import sys
input = sys.stdin.readline

while True:
    password = input().rstrip()             # ← 개행문자 제거
    if password == 'end':                   # ← 이제 정확히 'end'와 비교 가능
        break

    vowels = 'aeiou'
    is_acceptable = True

    # 1. 모음 포함 검사
    if not any(v in password for v in vowels):
        is_acceptable = False

    # 2. 모음·자음 3연속 검사
    vowel_cnt = conso_cnt = 0
    for ch in password:
        if ch in vowels:
            vowel_cnt += 1
            conso_cnt = 0
        else:
            vowel_cnt = 0
            conso_cnt += 1
        if vowel_cnt == 3 or conso_cnt == 3:
            is_acceptable = False
            break

    # 3. 같은 글자 연속 검사 (ee, oo 예외 허용)
    if is_acceptable:
        for i in range(1, len(password)):
            if password[i] == password[i-1] and password[i] not in {'e', 'o'}:
                is_acceptable = False
                break

    # 루프 안에서 바로 결과 출력
    if is_acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
