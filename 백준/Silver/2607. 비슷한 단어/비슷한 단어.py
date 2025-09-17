"""
두 단어가 같은 구성을 갖은 경우

1. 알파벳의 종류와 개수가 같음
2. 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우

DOG GOD GOOD DOLL x

모든 단어는 영문 알파벳, 대문자, 개수는 100개 이하, 길이는 10 이하

DOG,-> 1, 1, 1개
dictionary로 선언 -> -1, -1, -1, 

"""
import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

base = words[0]
base_len = len(base)

# 기준 단어 알파벳 빈도
alphabet = [0] * 26
for ch in base:
    alphabet[ord(ch) - ord('A')] += 1

cnt = 0
for w in words[1:]:
    if abs(base_len - len(w)) > 1:
        continue

    # 현재 단어의 빈도만큼 빼서 차이량 계산
    temp = alphabet[:]
    for ch in w:
        temp[ord(ch) - ord('A')] -= 1

    diff = sum(abs(x) for x in temp)  # 절댓값 합

    # 0: 완전 같은 구성, 1: 추가/삭제, 2: 교체
    if diff > 2:
        continue
    if diff == 2 and base_len != len(w):  # 교체는 길이가 같아야 성립
        continue

    cnt += 1

print(cnt)

    