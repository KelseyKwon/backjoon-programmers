from collections import defaultdict

def solution(participant, completion):
  hash_map = defaultdict(int)

  for i in participant:
    hash_map[i] += 1
  
  for name in completion:
    hash_map[name]-=1
  
  for name in hash_map:
    if (hash_map[name] > 0):
      return name