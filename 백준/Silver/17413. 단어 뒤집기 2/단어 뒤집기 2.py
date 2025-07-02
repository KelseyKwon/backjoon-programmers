import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip("\n")
    result = []     # 최종 문자열 조각을 여기에 append
    buffer = []     # 뒤집을 단어를 모아두는 곳
    in_tag = False  # 현재 '<' 안에 있는 중인지

    for ch in s:
        if ch == '<':           # 태그 시작
            # 1) 단어 버퍼에 남은 글자 뒤집어 result에 붙이기
            if buffer:
                result.extend(buffer[::-1])
                buffer.clear()
            # 2) 태그 모드로 전환 후 '<' 문자 추가
            in_tag = True
            result.append(ch)

        elif ch == '>':         # 태그 끝
            in_tag = False
            result.append(ch)

        else:
            if in_tag:
                # 태그 내부: 있는 그대로
                result.append(ch)
            else:
                # 태그 밖
                if ch == ' ':
                    # 공백: 앞에 모은 단어 뒤집어 붙이고 공백도 붙이기
                    result.extend(buffer[::-1])
                    buffer.clear()
                    result.append(' ')
                else:
                    # 단어 글자: 버퍼에 모으기
                    buffer.append(ch)

    # 반복 끝난 후에도 남은 단어가 있으면 뒤집어 붙이기
    if buffer:
        result.extend(buffer[::-1])

    # 결과 출력
    print("".join(result))


if __name__ == "__main__":
    solution()
