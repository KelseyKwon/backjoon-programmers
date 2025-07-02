from collections import deque

def solution(order):
    stack = []
    main = deque(range(1, len(order)+1))
    count = 0

    for want in order:
        # 1) 보조 벨트에 있다면 바로 꺼내기
        if stack and stack[-1] == want:
            stack.pop()
            count += 1

        else:
            # 2) 메인 벨트에서 꺼낼 때까지 보조 벨트로 이동
            while main and main[0] != want:
                stack.append(main.popleft())

            # 3) 메인 벨트에서 꺼낼 수 있으면 꺼내기
            if main and main[0] == want:
                main.popleft()
                count += 1
            # 4) 둘 다 아니면 중단
            else:
                break

    return count


