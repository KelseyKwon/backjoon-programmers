"""
양수, +, -, 괄호를 가지고 식을 만듦

0~9, +, -으로만, 그리고 처음과 마지막은 숫자이다. 

최소로 만들기.

큰수 -> 더하기를 먼저해. 

90-50-30 -> 10 

만약에 다 더하기야 -> 그럼 그냥 둬

90-50+30+20 이런식으로 섞여있어 -> 그러면 더하기부터 해.

90-50-30 이런식으로 빼기만 있어 -> 그러면 
80-30-60-70 -> -80, 
"""

import sys

math = sys.stdin.readline().strip().split('-')

hap = []
for i in math:
    # '+' 단위로 쪼개서 전부 더한 값만 남김
    temp = list(map(int, i.split('+')))
    hap.append(sum(temp))

result = hap[0]
for i in hap[1:]:
    result -= i

print(result)