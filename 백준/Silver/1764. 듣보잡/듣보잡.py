
import sys
input = sys.stdin.readline

not_heard = set()
not_seen  = set()

# 1) n, m을 정수로 읽기
n, m = map(int, input().split())

for _ in range(n):
    not_heard.add(input().strip())

for _ in range(m):
    not_seen.add(input().strip())

# 2) 교집합 구하고 정렬해서 출력
common = not_heard & not_seen
print(len(common))
for name in sorted(common):
    print(name)